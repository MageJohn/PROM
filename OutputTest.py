import time
import os
import random #Can be removed, just for demonstration

##Data required for each player: ADC value, Button states, Bat positions, and Super bat
##Other data required: Ball position, score

running=True

def printDiag(player1, player2, ball, score):
    print("\x1B[4;H|   1    |   {}    |   {}  |   {}  |   {}    |  {}   |".format(player1[0],player1[1],player1[2],player1[3],player1[4]))
    print("\x1B[5;H|   2    |   {}    |   {}  |   {}  |   {}    |  {}   |".format(player2[0],player2[1],player2[2],player2[3],player2[4]))
    print("\x1B[8;HBall Position: ({},{})".format(ball[0],ball[1]))
    print("\x1B[9;HScore: {}/{}".format(score[0],score[1]))
    
def playerCollate(adcVal, button1, button2, batPos, superBat):#collates player data into an array
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
    
print("\x1B[?1049h\x1B[2J\x1B[HDiagnostic Display for Pong")

print("\x1B[2;H \x1B[4m                                                               \x1B[m")#Prints top bar of table
print("\x1B[3;H| Player | ADC Val. | Button 1 | Button 2 | Bat Pos. | SuperBat |")
print("\x1B[6;H ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")#Prints bottom bar of table


while(running):
    player1 = playerCollate(random.randrange(255),False,True,random.randrange(24),False)
    player2 = playerCollate(255,True,False,24,True)
    printDiag(player1, player2, [2,5], [2,1])
    time.sleep(0.1)#small delay for each update, can be removed
    
    
