class Diagnostics:
    def __init__(self, player1, player2, ball):
        print("\x1B[?1049h\x1B[2J\x1B[HDiagnostic Display for Pong")

        print("\x1B[2;H \x1B[4m                                                               \x1B[m")#Prints top bar of table
        print("\x1B[3;H| Player | ADC Val. | Button 1 | Button 2 | Bat Pos. | SuperBat |")
        print("\x1B[6;H ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")#Prints bottom bar of table
        self.p1 = player1
        self.p2 = player2
        self.ball = ball

    def print_diag(self):
        iface = self.p1.interface
        player1 = self.player_collate(iface.knob.value,
                                 iface.serve_button.value,
                                 iface.superbat_button.value,
                                 iface.knob.bat_y,
                                 self.p1.bat._superbat)
        iface = self.p2.interface
        player2 = self.player_collate(iface.knob.value,
                                 iface.serve_button.value,
                                 iface.superbat_button.value,
                                 iface.knob.bat_y,
                                 self.p2.bat._superbat)
        ball = self.ball.pos
        score = [self.p1.score.score,self.p2.score.score]
        
        print("\x1B[4;H|   1    |   {0[0]}   |   {0[1]}  |   {0[2]}  |   {0[3]}    |  {0[4]}   |".format(player1))
        print("\x1B[5;H|   2    |   {0[0]}   |   {0[1]}  |   {0[2]}  |   {0[3]}    |  {0[4]}   |".format(player2))
        print("\x1B[8;HBall Position: ({0[0]},{0[1]})".format(ball))
        print("\x1B[9;HScore: {0[0]}/{0[1]}".format(score))

    def player_collate(self, adcVal, button1, button2, batPos, superBat):#collates player data into an array
        if button1:#Colours button 1 red or green
            button1s = "\x1B[32m"+str(button1)+" \x1B[0m"
        else:
            button1s = "\x1B[31m"+str(button1)+"\x1B[0m"
            
        if button2:#Colours button 2 red or green
            button2s = "\x1B[32m"+str(button2)+" \x1B[0m"
        else:
            button2s = "\x1B[31m"+str(button2)+"\x1B[0m"

        if superBat:#Colours superbat red or green
            superBats = "\x1B[32m"+str(superBat)+" \x1B[0m"
        else:
            superBats = "\x1B[31m"+str(superBat)+"\x1B[0m"
            
        player=[str(adcVal).center(4), str(button1s).center(5), str(button2s).center(5), str(batPos).center(3), str(superBats).center(5)]
        #centers all the values
        return player
        

