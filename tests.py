import sys
import time

from consolegraphics import ConsoleGraphics
import constants
import gameobj_score as score
import gameobj_net as net
import gameobj_bat as bat
import gameobj_ball as ball

import textserial

class TestOut:
    def __init__(self):
        self.total_written = 0

    def write(self, s):
        sys.stdout.write(s)
        self.total_written += len(s.encode())

    def flush(self):
        sys.stdout.flush()


def test_net():
    out = textserial.TextSerial("/dev/ttyAMA0", 115200)
    cg = ConsoleGraphics(output=out)
    n = net.Net(cg, constants.NET_COL)
    with cg:
        n.draw()
        cg.out.flush()
        time.sleep(1)


def test_ball():
    out = TestOut()
    writes = []
    cg = ConsoleGraphics(output=out)
    b = ball.Ball(cg, None, constants.BALL_COL)
    with cg:
        for i in range(10):
            b.draw()
            b.move()
            cg.out.flush()
            writes.append(out.total_written - sum(writes))
            time.sleep(0.5)
    print(', '.join([str(i) for i in writes]))


def test_bat():
    out = TestOut()
    cg = ConsoleGraphics(output=out)
    writes = []
    bat1 = bat.Bat(cg, bat.Bat.LEFT, constants.BAT_COL)
    bat2 = bat.Bat(cg, bat.Bat.RIGHT, constants.BAT_COL)
    with cg:
        writes.append(out.total_written - sum(writes))
        for i in range(5, -11, -1):
            bat1.draw()
            writes.append(out.total_written - sum(writes))
            bat2.draw()
            writes.append(out.total_written - sum(writes))
            bat1.move(bat1.y - (1 if i > 0 else -1))
            bat2.move(bat2.y + (1 if i > 0 else -1))
            cg.out.flush()
            time.sleep(0.5)
    print(', '.join([str(i) for i in writes]))


def test_score():
    out = TestOut()
    cg = ConsoleGraphics(output=out)
    writes = []
    score1 = score.Score(cg, score.Score.LEFT, constants.SCOR_COL)
    score2 = score.Score(cg, score.Score.RIGHT, constants.SCOR_COL)
    score2.score = 9
    with cg:
        writes.append(out.total_written - sum(writes))
        for i in range(10):
            score1.draw()
            writes.append(out.total_written - sum(writes))
            score2.draw()
            writes.append(out.total_written - sum(writes))
            score1.score += 1
            score2.score -= 1
            cg.out.flush()
            time.sleep(0.5)
    print(', '.join([str(i) for i in writes]))


def test_ball_over_score_net():
    out = TestOut()
    cg = ConsoleGraphics(output=out)
    s = score.Score(cg, score.Score.LEFT, constants.SCOR_COL)
    n = net.Net(cg, constants.NET_COL)
    b = ball.Ball(cg, None, constants.BALL_COL)
    b.pos = [1, s.side]
    with cg:
        s.draw()
        n.draw()
        for i in range(15):
            b.draw()
            b.move()
            cg.out.flush()
            time.sleep(0.5)


def test_ball_serve():
    out = TestOut()
    cg = ConsoleGraphics(output=out)
    bat1 = bat.Bat(cg, bat.Bat.LEFT, constants.BAT_COL)
    bat2 = bat.Bat(cg, bat.Bat.RIGHT, constants.BAT_COL)
    b = ball.Ball(cg, bat1, constants.BALL_COL)
    b.serving = True
    with cg:
        bat2.draw()
        for i in range(-5, 11):
            bat1.move(bat1.y + (-1 if i < 1 else 1))
            b.move()
            bat1.draw()
            b.draw()
            cg.out.flush()
            time.sleep(0.2)
        b.serving = False
        for i in range(5):
            b.move()
            b.draw()
            cg.out.flush()
            time.sleep(0.2)
        b.serving = True
        b.server = bat2
        for i in range(-5, 11):
            bat2.move(bat2.y + (-1 if i < 1 else 1))
            b.move()
            bat2.draw()
            b.draw()
            cg.out.flush()
            time.sleep(0.2)


def test_ball_collide():
    out = TestOut()
    cg = ConsoleGraphics(output=out)
    bat1 = bat.Bat(cg, bat.Bat.LEFT, constants.BAT_COL)
    bat2 = bat.Bat(cg, bat.Bat.RIGHT, constants.BAT_COL)
    b = ball.Ball(cg, None, constants.BALL_COL)

    trials = (([bat1.y - 4, bat1.col + 4], [1, -1]),
              ([bat1.y - 3, bat1.col + 4], [1, -1]),
              ([bat1.y - 2, bat1.col + 4], [1, -1]),
              ([bat1.y - 1, bat1.col + 4], [1, -1]),
              ([bat1.y,     bat1.col + 4], [1, -1]),
              ([bat2.y - 4, bat2.col - 4], [1,  1]),
              ([bat2.y - 3, bat2.col - 4], [1,  1]),
              ([bat2.y - 2, bat2.col - 4], [1,  1]),
              ([bat2.y - 1, bat2.col - 4], [1,  1]),
              ([bat2.y,     bat2.col - 4], [1,  1]),
              ([5, 36], [-1, 1]),
              ([16, 36], [1, 1]))
    with cg:
        for pos, vector in trials:
            b.pos = pos
            b.vector = vector
            for i in range(8):
                bat1.draw()
                bat2.draw()
                b.draw()

                b.move()

                new_vec = bat1.collide(b) or bat2.collide(b) or b.collide()
                if new_vec:
                    b.vector = new_vec

                cg.out.flush()
                time.sleep(0.2)
            time.sleep(0.5)


def test_bg_memory():
    # Tests whether the dictionary used to keep track of what's in the
    # background (for updating the ball) is correct
    cg = ConsoleGraphics()
    s1 = score.Score(cg, score.Score.LEFT, constants.SCOR_COL)
    s2 = score.Score(cg, score.Score.RIGHT, constants.SCOR_COL)
    n = net.Net(cg, constants.NET_COL)

    with cg:
        n.draw()
        s1.draw()
        s2.draw()
        for i in range(10):
            cg.out.flush()
            time.sleep(0.5)
            cg.write("\x1B[49m\x1B[2J")  # Clear the screen
            for k in cg.bg:
                # Move to position
                cg.write("\x1B[{};{}H".format(k[0], k[1]))
                # Set background color from the dictionary
                cg.write("\x1B[{}m".format(cg.bg[k]))
                cg.write(' ')
            cg.out.flush()
            time.sleep(0.5)
            if i % 2 == 0:
                s1.score += 1
                s1.draw()
            else:
                s2.score += 1
                s2.draw()
