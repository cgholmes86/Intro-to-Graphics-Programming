from Tkinter import *
import slotmachine_0_1
'''
Programmer : Clay Holmes
Created : June 3, 2013
Last Modified : June 7, 2013
Filename : slotmachine_v3.py
Version : 3.0
'''

#Adapted from "nesting.py" found in Lesson 05 code -CH

class MyApp:
    def __init__(self, parent):

        self.myParent = parent
        
        #Parent frame called slotContainer - CH
        self.slotContainer = Frame(parent)
        self.slotContainer.pack()
        
        myimage = PhotoImage(file="8bit.gif")
        self.label1 = Label(self.slotContainer)
        self.label1.configure(image=myimage)
        self.label1.image = myimage
        self.label1.pack()
        
        buttonTest = Button(self, text="Test")
        buttonTest.place(x=100, y=100)

        #These constants will be used to control the size and shape of buttons - CH
        #------ constants for controlling layout ------
        button_width = 6 #width in characters

        #padding is extra space the goes around the text
        button_padx = "2m" #button padding in millimeters
        button_pady = "1m" 
        buttons_frame_padx = "3m" #outside frame padding in millimeters
        buttons_frame_pady = "2m" 
        buttons_frame_ipadx = "3m" #internal frame padding in millimeters
        buttons_frame_ipady = "1m" 
        # -------------- end constants ----------------

        #We will use VERTICAL (top/bottom) orientation inside slotContainer.
        #Inside slotContainer, first we create buttons_frame.
        #Then we create top_frame and bottom_frame.
        #These will be our demonstration frames.
        
        #The buttons frame will sit at the bottom of the slotContainer frame - CH
        
        # buttons frame
        self.buttons_frame = Frame(self.slotContainer) ###
        self.buttons_frame.pack(
            side=BOTTOM, ###
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            padx=buttons_frame_padx,
            pady=buttons_frame_pady,
            )

        #The top frame will be above the "main" frame and houses the Start and Quit buttons
        # top frame
        self.top_frame = Frame(self.slotContainer)
        self.top_frame.pack(side=TOP,
            fill=BOTH,
            expand=YES,
            )
        
        '''
        #This is the "Main" frame where the image of the slot machine is placed        
        # bottom frame
        self.bottom_frame = Frame(self.slotContainer,
            borderwidth=5, relief=RIDGE,
            height=600,
            width=800,
            background="white",
            )
        
        self.bottom_frame.pack(side=TOP,
            fill=BOTH,
            expand=YES,
            )
        '''
        #Now we will put two more frames, left_frame and right_frame,
        #inside top_frame. We will use HORIZONTAL (left/right)
        #orientation within top_frame.
        
        # upper_frame
        self.upper_frame = Frame(self.top_frame, background="white",
            borderwidth=5, relief=RIDGE,
            height=50,
            width=800,
            ) 

        self.upper_frame.pack(side=TOP,
            fill=BOTH,
            expand=YES,
            ) 

        testText = StringVar()
        self.label1 = Label(self.slotContainer)
        self.label1.configure(textvariable=testText)
        testText.set("Jackpot: ")
        self.label1.pack()
                
        # now we add the buttons to the buttons_frame
        self.button1 = Button(self.buttons_frame, command=self.button1Click)
        self.button1.configure(text="Bet $50", background= "green")
        self.button1.focus_force()
        self.button1.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )

        self.button1.pack(side=LEFT)
        self.button1.bind("<Return>", self.button1Click_a)
        
        self.button2 = Button(self.buttons_frame, command=self.button2Click)
        self.button2.configure(text="Bet $100", background="green")
        self.button2.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady 
            )

        self.button2.pack(side=LEFT)
        self.button2.bind("<Return>", self.button2Click_a)
        
        self.button3 = Button(self.buttons_frame, command=self.button3Click)
        self.button3.configure(text="Bet $500", background="green")
        self.button3.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
           )
        
        self.button3.pack(side=LEFT)
        self.button3.bind("<Return>", self.button3Click_a)
        
        self.button4 = Button(self.buttons_frame, command=self.button4Click)
        self.button4.configure(text="Bet $1000", background="green")
        self.button4.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
           )
        
        self.button4.pack(side=LEFT)
        self.button4.bind("<Return>", self.button4Click_a)
        
        self.button5 = Button(self.buttons_frame, command=self.button5Click)
        self.button5.configure(text="Spin", background="yellow")
        self.button5.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
           )
        
        self.button5.pack(side=RIGHT)
        self.button5.bind("<Return>", self.button5Click_a)
        
        self.button6 = Button(self.upper_frame, command=self.button6Click)
        self.button6.configure(text="Quit", background="red")
        self.button6.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
           )
        
        self.button6.pack(side=TOP)
        self.button6.bind("<Return>", self.button6Click_a)
        
        self.button7 = Button(self.upper_frame, command=self.button7Click)
        self.button7.configure(text="Start", background="blue")
        self.button7.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
           )
        
        self.button7.pack(side=TOP)
        self.button7.bind("<Return>", self.button7Click_a)
        
        #button functionality

    def button1Click(self):
        print("Button1 has been clicked")
        #testing to see if the slotmachin_0_1.py code could read the button inputs
        print(slotmachine_0_1.is_number(50))        
            
    def button2Click(self):
        print("Button2 has been clicked")
        
    def button3Click(self):
        print("Button3 has been clicked")
            
    def button4Click(self):
        print("Button4 has been clicked")
    #Reels spun and printed to the console        
    def button5Click(self):
        print(slotmachine_0_1.Reels())

    def button6Click(self):
        self.myParent.destroy()
    #playing around with trying to initiate functionality
    def button7Click(self):
        print("I tried")

    def button1Click_a(self, event):
        self.button1Click()

    def button2Click_a(self, event):
        self.button2Click()
        
    def button3Click_a(selfself, event):
        self.button3Click()
        
    def button4Click_a(selfself, event):
        self.button4Click()
        
    def button5Click_a(selfself, event):
        self.button5Click()
        
    def button6Click_a(selfself, event):
        self.button6Click()
        
    def button7Click_a(selfself, event):
        self.button7Click()

def main():
    root = Tk()
    root.title("My Slot Machine")
    myapp = MyApp(root)
    root.mainloop()
    

if __name__ == "__main__": main()