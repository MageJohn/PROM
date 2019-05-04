import time

from .consolegraphics import ConsoleGraphics
from . import constants
from .inputs import ai
from .game_objects.net import Net
from .game_objects.ball import Ball
from .player import Player


def main():
    """Main function of the game. Contains the game loop and logic"""
    cg = ConsoleGraphics(output=constants.OUTPUT)

    net = Net(cg, constants.NET_COL)
    ball = Ball(cg, constants.BALL_COL)

    p1 = Player(cg, ball, constants.LEFT, constants.P1_INTERFACE)
    p2 = Player(cg, ball, constants.RIGHT, constants.P2_INTERFACE)

    if type(p1.interface) is ai.AI:
        p1.interface.give_inputs(ball, p1.bat)
    if type(p2.interface) is ai.AI:
        p2.interface.give_inputs(ball, p2.bat)

    serves = 5
    ball.serving = True
    ball.server = p1.bat

    with cg:
        net.draw()
        p1.score.draw()
        p2.score.draw()
        p1.bat.draw()
        p2.bat.draw()

        # Code goes here for intro music

        # Independant refresh times mean the ball can change speeds without
        # affecting the bats.
        ball_refresh_time = time.perf_counter()
        bat_refresh_time = time.perf_counter()

        playing = True
        while playing:
            if time.perf_counter() - ball_refresh_time >= ball.speed:
                if ball.pos[1] == 0 or ball.pos[1] == constants.SCR_WIDTH:
                    if ball.pos[1] == 0:
                        p2.score.score += 1
                        p2.score.draw()
                    else:
                        p1.score.score += 1
                        p1.score.draw()

                    ball.serving = True
                    ball.speed = constants.BAT_SPEED
                    serves -= 1
                    if not serves:
                        ball.server = p2.bat \
                                        if ball.server is p1.bat else \
                                        p1.bat
                        serves = 5

                    if p1.score.score == 9 or p2.score.score == 9:
                        playing = False

                    # Code goes here for score events; e.g. PiGlow lights,
                    # sound effects

                elif not ball.just_served and not ball.serving:
                    bat_collide = p1.bat.collide(ball) or\
                                  p2.bat.collide(ball)
                    wall_collide = ball.collide()
                    if bat_collide:
                        ball.vector = bat_collide
                        ball.randomise_speed()
                    if wall_collide:
                        ball.vector = wall_collide
                if ball.just_served:
                    ball.just_served = False

                    # Code goes here for bounce events; e.g. sound effects

                ball.move()

                # Code goes here for LEDs indicating ball pos

                ball.draw()

                ball_refresh_time = time.perf_counter()

            if time.perf_counter() - bat_refresh_time >= constants.BAT_SPEED:
                # Move bats to position here

                p1.update()
                p2.update()

                p1.bat.draw()
                p2.bat.draw()

                bat_refresh_time = time.perf_counter()

            # Possible place for code which deals with smoothing

            if constants.FLUSHING:
                # flush updates to screen
                cg.out.flush()


if __name__ == "__main__":
    main()