import time
import os

def print_diag():
    time.sleep(1)
    player1 = player_collate(p1.interface.knob.value,False,True,3,False)
    player2 = player_collate(255,True,False,24,True)
    ball = [1,5]
##    ball = [ball.pos[0],ball.pos[1]]
    score = [3,4]#score.score
    
    print("\x1B[4;H|   1    |   {}    |   {}  |   {}  |   {}    |  {}   |".format(player1[0],player1[1],player1[2],player1[3],player1[4]))
    print("\x1B[5;H|   2    |   {}    |   {}  |   {}  |   {}    |  {}   |".format(player2[0],player2[1],player2[2],player2[3],player2[4]))
    print("\x1B[8;HBall Position: ({},{})".format(ball[0],ball[1]))
    print("\x1B[9;HScore: {}/{}".format(score[0],score[1]))
    
def player_collate(adcVal, button1, button2, batPos, superBat):#collates player data into an array
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
        
    player=[str(adcVal).center(3), str(button1s).center(5), str(button2s).center(5), str(batPos).center(3), str(superBats).center(5)]
    #centers all the values
    return player
    

