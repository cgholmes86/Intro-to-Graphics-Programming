#Programmer : Clay Holmes
#Date : May 9, 2013
#Program name : Name printer
#Filename : printName.py
#Python version : 3.3

def main():
    #when using python 2.7, switch input to raw_input
    userName = input("Please tell me your name: ")
    print ("I will shout your name: ", userName.upper())
    print ("Now all in lowercase: ", userName.lower())
    print ("How about inverting the case? ", userName.swapcase())
    numChars = len(userName)
    print ("Your name has", numChars, "characters")
    print ("Now I'll pronounce your name like a cartoon character: ")
    userName = userName.upper()
    userName = userName.replace("R", "W")
    userName = userName.title()
    print (userName)

if __name__ == "__main__": main()
