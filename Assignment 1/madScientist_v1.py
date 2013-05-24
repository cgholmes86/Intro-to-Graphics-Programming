'''
Programmer : Clay Holmes
Created : May 15, 2013
Last Modified : May 22, 2013
Filename : madScientist_v2.py

'''
import time

#The 14 possible locations the player can go to 
playerPositions = ["labCurtains",    #0
                   "frontDoor",      #1
                   "sideLawn",       #2
                   "frontLawn",      #3
                   "hallCloset",     #4
                   "sideDoor",       #5
                   "office",         #6
                   "labDoor",        #7
                   "basementMain",   #8
                   "basementCellar", #9
                   "stormDoor",      #10
                   "upStairs",       #11
                   "attic",        #12
                   "upstairsOffice"  #13                                
                  ]


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

def playerMove():
        
    move = ''
    while move !='1' and move !='2':
        print ("Which path will you choose?")
        move = int(raw_input())
        i = move
        
        for i in range(len(playerPositions)):
            playerPosition = playerPositions[i]
            
            return move 
    
def chooseMove(playerPosition):
           
    if playerPosition == "labCurtains":
        print ("You decide to hide behind some curtains in the lab and wait and see")
        print ("what the noise is coming from.  You see a shadowy figure through")
        print ("the curtains, but they leave the room soon after.")
        print ("Your choices are to head out into the hall and hide in the closet (1)")
        print ("                   -or-                                              ")
        print ("Run to the front door (2)")
        playerMove()
        
    elif playerPosition == "labDoor":
        print ("You decide to head straight for the lab door, hoping no one sees you.")
        print ("Once out in the hall you hear some noise but don't know where it is")
        print ("coming from, but you need to make a decision as soon as possible before")
        print ("whatever is making that noise finds you!  You see two stairways in your view.")
        print ("Your choices are to head to the stairs leading up (1)")
        print ("                  -or-                                               ")
        print ("Head to the stairs leading down (2)")
        playerMove()
        
    elif playerPosition == "frontDoor":
        print ("You run as fast as you can to the front door, running through the hall to")
        print ("get to it.  Once outside, you see a brightly lit driveway ahead of you")
        print ("and a moonlit lawn to your right.  You can sense that danger is still behind")
        print ("you and must make a decision quickly!")
        print ("Your choices are to run onto the driveway and try and make it to the road (1)")
        print ("                 -or-                                                ")
        print ("Run to the side of the house and escape across the river (2).")
        playerMove()
    
    elif playerPosition == "hallCloset":
        print ("You hide in the hall closet, hoping that whatever it is that you heard has")
        print ("gone by.  Once you stop hearing movement, you decide to open the door and ")
        print ("make your next move.  You see two doors in front of you and hearing another")
        print ("noise you and must make your decision quickly!")
        print ("Your choices are to head to the door to your left (1)")
        print ("                 -or-                                                ")
        print ("Head to the door to your right (2).")
        playerMove()
        
    elif playerPosition == "basementMain":
        print ("You head downstairs thinking there could be an secret door to the outside.")
        print ("You start hearing footsteps behind you on the stairs and must make your")
        print ("decision fast!")
        print ("Your choices are to hide out in the basement cellar (1)")
        print ("                 -or-                                                ")
        print ("Run and try and pry open the storm door on the opposite side of the basement (2).")
        
    elif playerPosition == "upstairs":
        print ("You decide to head upstairs thinking that maybe you could escape through")
        print ("a window in a bedroom.  You notice that all of the doors except 1 are boarded up")
        print ("and the attic door is open with a ladder leading up.  You hear someone approaching on")
        print ("the stairs behind you.  Think quick!")
        print ("Your choices are to open the one door and hope there is a window in there to escape through (1)")
        print ("                 -or-                                                ")
        print ("Climb up into the attic and hope to escape through there somehow (2).")
        playerMove()
    
    elif playerPosition == "basementCellar":
        print ("The door behind you slams shut.  You see a bloody operating table in the center of the room")
        print ("and through a hole in the wall behind you the Mad Scientist creepily says")
        print ("You're trapped now, soon you will be my next experiment, as originally intended!")
        print ("Game over!")
        playerMove()
        
    elif playerPosition == "stormDoor":
        print ("You push and tug on the door as hard as you can, but it simply won't budge.")
        print ("A hand lands on your shoulder, spinning you around.  The Mad Scientist shouts")
        print ("GOTCHA! and clubs you over the head.")
        print ("Game over!")
        playerMove()
        
    elif playerPosition == "attic":
        print ("You run up into the attic, hoping for some kind of escape.  Instead you find")
        print ("one of the Mad Scientist's monsters, a half man half shark who grabs you and ")
        print ("eats you whole!")
        print ("Game over!")
        
    elif playerPosition == "upstairsOffice":
        print ("You open the door and see bars over the window.  Oh no!  You turn around and")
        print ("receive a face full of knock-out gas from the Mad Scientist.  You wake up hours")
        print ("later back on the operation table, this time securly strapped in.")
        print ("Game over!")
        
    elif playerPosition == "sideDoor":
        print ("You head to the door on your left and it leads to the outside!  But as you step")
        print ("you fall into a deep pit with alligators at the bottom and they eat you up!")
        print ("Game over!")
        
    elif playerPosition == "office":
        print ("You head to the door on you right and it leads to an office.  You see that someone")
        print ("is sitting in the chair at the desk, turned away from you.  You approach and spin")
        print ("the chair around.  It's the Mad Scientist!  He punches you in the face and then")
        print ("hits you over the head with a bat.  You wake up hours later back on the operating")
        print ("table, this time securly strapped in.")
        print ("Game over!")
        
    elif playerPosition == "frontLawn":
        print ("You decide to run for the driveway and across the front lawn.  As you are running,")
        print ("you hear viscious dogs behind you.  They catch up in no time, tackling you to the ground.")
        print ("The Mad Scientist is close behind and ties you up, bringing you back to the operating")
        print ("table, making sure to strap you in tight this time.")
        print ("Game over!")
        
    elif playerPosition == "sideLawn":
        print ("You decide to run for the river at the side of the house.  As you are running, you hear ")
        print ("viscious dogs behind you.  You jump into the river and began swimming, hoping for some ")
        print ("kind of luck.  As you get to the opposite side of the river, you look back and see that")
        print ("the dogs are afraid of water.  You run out onto the road nearby and wave down a car.")
        print ("You tell the driver about your horrific tale and he drives you to the nearest police")
        print ("station so you can file a report on the Mad Scientist.")
        print ("Congratulations, you escaped!")

def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        playerPosition = "labTable"
        print ("You hear some noise outside the door.  You can either hide behind (1)")
        print ("some curtains in the room or run out into the hall to see what to do (2).")
        choosePath = playerMove()
        chooseMove(playerPosition)
    
        print ('Do you want to attempt your escape again? (yes or no)')
        playAgain = raw_input()
    print ("Thanks for Playing!")
    print ("Game Design by Clay Holmes")
    


if __name__ == "__main__" : main()