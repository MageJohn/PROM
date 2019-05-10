import time

import constants
from consolegraphics import ConsoleGraphics
from inputs.ai import AI
from game_objects.net import Net
from game_objects.ball import Ball
from player import Player
from sound.note import Note
from diagdisplay import Diagnostics

if constants.COUNTDOWN:
    from countdown import Countdown

if constants.BALL_LEDS:
    from ball_leds import BallLEDs

if constants.PIGLOW:
    from lights import pulse_all

if not constants.P1_AI or not constants.P2_AI:
    from inputs.ad799_knob import AD799
    from inputs.diy_knob import DIY_ADC
    from inputs.i2c_button import I2C_Button
    from inputs.interface import HardwareInputs


def main():
    """Main function of the game. Contains the game loop and logic"""
    cg = ConsoleGraphics(output=constants.OUTPUT)

    net = Net(cg, constants.NET_COL)
    ball = Ball(cg, constants.BALL_COL)

    if constants.BALL_LEDS:
        ball_leds = BallLEDs()

    if constants.PIGLOW:
        pulse = pulse_all.PulseLights()

    if not constants.P1_AI:
        p1_knob = AD799(constants.AD799_ADDR)
        p1_serve = I2C_Button(constants.BUTTON2_ADDR,
                              constants.BUTTON2_BIT,
                              constants.BUTTON2_ACTIVE_LOW,
                              debounce=False)
        p1_superbat = I2C_Button(constants.BUTTON3_ADDR,
                                 constants.BUTTON3_BIT,
                                 constants.BUTTON3_ACTIVE_LOW,
                                 debounce=False)
        p1_interface = HardwareInputs(p1_knob,
                                      p1_serve,
                                      p1_superbat)
    else:
        p1_interface = AI(ball=ball)

    if not constants.P2_AI:
        p2_knob = DIY_ADC(constants.I2C_BUS,
                          constants.DIY_ADC_PIN,
                          constants.DIY_ADC_ADDR,
                          constants.DIY_ADC_N_BITS)
        p2_serve = I2C_Button(constants.BUTTON0_ADDR,
                              constants.BUTTON0_BIT,
                              constants.BUTTONS_P2_ACTIVE_LOW,
                              debounce=True)
        p2_superbat = I2C_Button(constants.BUTTON1_ADDR,
                                 constants.BUTTON1_BIT,
                                 constants.BUTTONS_P2_ACTIVE_LOW,
                                 debounce=True)
        p2_interface = HardwareInputs(p2_knob,
                                      p2_serve,
                                      p2_superbat)
    else:
        p2_interface = AI(ball=ball)

    p1 = Player(cg, ball, constants.LEFT, p1_interface)
    p2 = Player(cg, ball, constants.RIGHT, p2_interface)

    # sound = constants.SOUND(constants.SOUND_PIN)
    # sound.notes(constants.INTRO_MUS)

    if type(p1.interface) is AI:
        p1.interface.give_inputs(bat=p1.bat)
    if type(p2.interface) is AI:
        p2.interface.give_inputs(bat=p2.bat)

    diag = Diagnostics(p1, p2, ball)

    serves = constants.N_SERVES
    ball.serving = True
    ball.server = p1.bat

    with cg:
        net.draw()
        p1.score.draw()
        p2.score.draw()
        p1.bat.draw()
        p2.bat.draw()
        if constants.FLUSHING:
            cg.out.flush()


        # Countdown on the 7-seg display. Blocking, so game starts when
        # it finishes
        if constants.COUNTDOWN:
            cd = Countdown(constants.I2C_BUS, constants.COUNTDOWN_ADDR,
                           constants.COUNTDOWN_N_BITS, constants.COUNTDOWN_LSB,
                           constants.COUNTDOWN_SPEED)
            cd.activate()

        # Code goes here for intro music

        # Independant refresh times mean the ball can change speeds without
        # affecting the bats.
        ball_refresh_time = time.perf_counter()
        input_refresh_time = time.perf_counter()

        playing = True
        while playing:
            if time.perf_counter() - ball_refresh_time >= ball.speed:
                if (ball.pos[1] == constants.SCR_MIN or
                        ball.pos[1] == constants.SCR_WIDTH):
                    if ball.pos[1] == constants.SCR_MIN:
                        p2.score.score += 1
                        p2.score.draw()
                        if constants.PIGLOW:
                            pulse.activate()
                    else:
                        p1.score.score += 1
                        p1.score.draw()
                        if constants.PIGLOW:
                            pulse.activate()

                    ball.serving = True
                    ball.speed = constants.BAT_SPEED
                    serves -= 1
                    if not serves:
                        ball.server = p2.bat \
                                        if ball.server is p1.bat else \
                                        p1.bat
                        serves = constants.N_SERVES

                    if (p1.score.score == constants.WIN_SCORE or
                            p2.score.score == constants.WIN_SCORE):
                        playing = False

                    # Code goes here for score events; e.g. PiGlow lights,
                    # sound effects

                elif not ball.just_served and not ball.serving:
                    bat_collide = p1.bat.collide(ball) or\
                                  p2.bat.collide(ball)
                    wall_collide = ball.collide()
                    if bat_collide:
                        ball.randomise_speed()
                        # sound.note(Note(constants.BAT_TONE, constants.TONE_LENGTH))
                    if wall_collide:
                        pass
                        # sound.note(Note(constants.WALL_TONE, constants.TONE_LENGTH))
                if ball.just_served:
                    ball.just_served = False

                    # Code goes here for bounce events; e.g. sound effects

                ball.move()

                if constants.BALL_LEDS:
                    ball_leds.update(ball.pos[1])

                # Code goes here for LEDs indicating ball pos

                ball.draw()

                ball_refresh_time = time.perf_counter()

            if time.perf_counter() - input_refresh_time >= constants.BAT_SPEED:
                # Move bats to position here

                p1.update()
                p2.update()

                if constants.DEBUG:
                    diag.print_diag()

                p1.bat.draw()
                p2.bat.draw()

                input_refresh_time = time.perf_counter()

            if constants.FLUSHING:
                # flush updates to screen
                cg.out.flush()

            # sound.update()
    if p1.score.score == constants.WIN_SCORE:
        winner = "Player 1"
    if p2.score.score == constants.WIN_SCORE:
        winner = "Player 2"
    print("The winner is {}".format(winner))


if __name__ == "__main__":
    main()
