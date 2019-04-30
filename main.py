import time
import random

from graphics_shim import ConsoleGraphics
import constants
from score import Score
from net import Net
from bat import Bat
from ball import Ball
from ai import AI

if not (constants.AI_P1 and constants.AI_P2):
    import input_interface


def main():
    """Main function of the game. Contains the game loop and logic"""
    cg = ConsoleGraphics(output=constants.OUTPUT)

    net = Net(cg, constants.NET_COL)
    p1_score = Score(cg, Score.LEFT, constants.SCOR_COL)
    p2_score = Score(cg, Score.RIGHT, constants.SCOR_COL)
    p1_bat = Bat(cg, Bat.LEFT, constants.BAT_COL)
    p2_bat = Bat(cg, Bat.RIGHT, constants.BAT_COL)
    ball = Ball(cg, p1_bat, constants.BALL_COL)

    if not (constants.AI_P1 and constants.AI_P2):
        p1_interface = input_interface.AD799()

    ai1 = AI(ball, p1_bat)
    ai2 = AI(ball, p2_bat)

    serves = 5
    serve = False
    ball.serving = True

    with cg:
        net.draw()
        p1_score.draw()
        p2_score.draw()
        p1_bat.draw()
        p2_bat.draw()

        # Code goes here for intro music

        # Independant refresh times mean the ball can change speeds without
        # affecting the bats.
        ball_refresh_time = time.perf_counter()
        bat_refresh_time = time.perf_counter()
        ai_refresh_time = time.perf_counter()

        playing = True
        while playing:
            if time.perf_counter() - ball_refresh_time >= ball.speed:
                if ball.pos[1] == 0 or ball.pos[1] == constants.SCR_WIDTH:
                    if ball.pos[1] == 0:
                        p2_score.score += 1
                        p2_score.draw()
                    else:
                        p1_score.score += 1
                        p1_score.draw()

                    ball.serving = True
                    ball.speed = constants.BAT_SPEED
                    serves -= 1
                    if not serves:
                        ball.server = p2_bat \
                                        if ball.server is p1_bat else \
                                        p1_bat
                        serves = 5

                    if p1_score.score == 9 or p2_score.score == 9:
                        playing = False

                    # Code goes here for score events; e.g. PiGlow lights,
                    # sound effects

                elif not serve and not ball.serving:
                    bat_collide = p1_bat.collide(ball) or\
                                  p2_bat.collide(ball)
                    wall_collide = ball.collide()
                    if bat_collide:
                        ball.vector = bat_collide
                        ball.randomise_speed()
                    if wall_collide:
                        ball.vector = wall_collide

                        # Code goes here for bounce events; e.g. sound effects
                elif serve:
                    serve = False
                    ball.serving = False
                    ball.vector = [random.choice([-1, 0, 1]), ball.server.side]

                ball.move()

                # Code goes here for LEDs indicating ball pos

                ball.draw()

                ball_refresh_time = time.perf_counter()

            if time.perf_counter() - bat_refresh_time >= constants.BAT_SPEED:
                # Move bats to position here

                if not constants.AI_P1:
                    p1_input = p1_interface.get_input()
                    p1_bat.move(p1_input[0])
                    if ball.server is p1_bat and p1_input[1] and ball.serving:
                        serve = True

                p1_bat.draw()
                p2_bat.draw()

                bat_refresh_time = time.perf_counter()

            if time.perf_counter() - ai_refresh_time >= constants.AI_SPEED:
                if constants.AI_P1:
                    ai1_input = ai1.get_input()
                    p1_bat.move(ai1_input[0])
                    if ball.server is p1_bat and ai1_input[1]:
                        serve = True
                if constants.AI_P2:
                    ai2_input = ai2.get_input()
                    p2_bat.move(ai2_input[0])
                    if ball.server is p2_bat and ai2_input[1]:
                        serve = True

                ai_refresh_time = time.perf_counter()

            # Possible place for code which deals with smoothing

            if constants.FLUSHING:
                # flush updates to screen
                cg.out.flush()


if __name__ == "__main__":
    main()
