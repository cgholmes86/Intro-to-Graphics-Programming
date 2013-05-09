#Programmer : Clay Holmes
#Date : May 9, 2013
#Program name : Cheese Shop
#Filename : cheeseShop.py
#Python version : 3.3

def main():
    #tell the user something
    print ("Welcome to the cheese shop!")

    #get information from the user
    cheeseType =input("What kind of cheese would you like? ")
    # * when using python 2.7, change input to raw_input

    #we don't have that kind of cheese
    print ("Sorry, we're all out of ")
    print cheeseType

if __name__ == "__main__": main()
