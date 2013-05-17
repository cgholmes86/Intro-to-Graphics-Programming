'''
Programmer : Clay Holmes
Created : May 15, 2013
Last Modified : May 15, 2013
Filename : madScientist.py

'''
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
    playerPosition = labTable

def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
    
        print ('Do you want to attempt your escape again? (yes or no)')
        playAgain = raw_input()
    print ("test")
    


if __name__ == "__main__" : main()