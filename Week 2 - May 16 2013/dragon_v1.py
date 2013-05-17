#Programmer : Clay Holmes
#Date : May 16, 2013
#Program name : Dragon Adventure
#File name : dragon.py
#Python version used : 2.7.4 

import random
import time

def displayIntro():
	print ('You are on a planet full of dragons. In front of you,')
	print ('you see three caves. In one cave, the dragon is friendly')
	print ('and will share his treasure with you. The second dragon')
	print ('is greedy and hungry, and will eat you on sight.')
	print ('The third dragon will hold you captive and bore you') 
	print ('to death with drawn-out tales of his former glory slaying knights.')
	print ('Good luck!')
	print
	
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2' and cave != '3':
		print ('Which cave will you go into? (1, 2, or 3)')
		cave = raw_input()
	return cave

def checkCave(chosenCave):
	print ('You approach the cave...')
	time.sleep(2)
	print ('It is dark and spooky...')
	time.sleep(2)
	print ('A large dragon jumps out in front of you! He opens his jaws and...')
	print
	time.sleep(2)
	
	friendlyCave = random.randint(1, 3)
	boringCave = random.randint(1,3)
	
	#friendlyCave = '1'
	#boringCave = '2'
	#badCave = '3'
	
	if chosenCave == str(friendlyCave):
		print ('Gives you his treasure!')
	elif chosenCave == str(boringCave):
		print ('Bores you to death with stories!')
	else:
		print ('Gobbles you down in one bite!')

def main():
	
	
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		caveNumber = chooseCave()
		checkCave(caveNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
