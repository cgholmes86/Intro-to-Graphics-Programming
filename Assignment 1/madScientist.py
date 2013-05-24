'''
Programmer : Clay Holmes
Created : May 15, 2013
Last Modified : May 22, 2013
Filename : madScientist.py

'''
import time

def displayIntro():
    print ('================================================================')
    print ('You wake up, finding yourself on an operating table')
    print ('inside a dimly-lit, cold laboratory.  You look to your')
    print ('left and see a pile of bodies, the unlucky ones who')
    print ('have been experimented on by some deranged scientist.')
    print ('Luckily you are not bound to your table and are free to') 
    print ('move off the table.  Your task is to escape the Mad Scientists')
    print ('house.  Make the wrong decision and he will find you and')
    print ('make you his next experiment.')
    print ('Good luck!')
    print ('================================================================')
    print

def player():
    
    for i in range(0, len(playerPositions)):
        something = playerPosition[i]
        move = iz
    
    
def decisionLevel():
    
    while playerPosition != "1" and playerPosition != "2":
        print ("Which way will you go?")
        playerPosition = raw_input()
    
def chooseMove():
    
    #The 14 possible locations the player can go to 
    playerPositions = [labCurtains,    #0
                       frontDoor,      #1
                       sideLawn,       #2
                       frontLawn,      #3
                       hallCloset,     #4
                       sideDoor,       #5
                       office,         #6
                       labDoor,        #7
                       basementMain,   #8
                       basementCellar, #9
                       stormDoor,      #10
                       upStairs,       #11
                       bedroom,        #12
                       upstairsOffice  #13                                
              ]
    
    if playerPosition == labCurtains:
        print "You decide to hide behind some curtains in the lab and wait and see"
        print "what the noise is coming from.  "
    
    print ""

def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        playerPosition = labTable
    
        print ('Do you want to attempt your escape again? (yes or no)')
        playAgain = raw_input()
    print ("Thanks for Playing!")
    print ("Game Design by Clay Holmes")
    


if __name__ == "__main__" : main()