'''
Created on May 23, 2013

@author: Clay
'''
import random

def diceFace():
    print "======="
    diceValues(1);
    print "======="
    
def diceOne():
    print "|     |"
    print "|  *  |"
    print "|     |"
    
def diceTwo():
    print "|*    |"
    print "|     |"
    print "|    *|"
    
def diceThree():
    print "|*    |"
    print "|  *  |"
    print "|    *|"
    
def diceFour():
    print "|*   *|"
    print "|     |"
    print "|*   *|"
    
def diceFive():
    print "|*   *|"
    print "|  *  |"
    print "|*   *|"
    
def diceSix():
    print "|*   *|"
    print "|*   *|"
    print "|*   *|"
    
def diceValues():
    diceOne = 1;
    diceTwo = 2;
    diceThree = 3;
    diceFour = 4;
    diceFive = 5;
    diceSix = 6;
    
def main():
    diceFace;
    
    if __name__ == "__main__" : main()