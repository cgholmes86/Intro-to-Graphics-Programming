from Tkinter import *
'''
Programmer : Clay Holmes
Created : May 28, 2013
Last Modified : May 30, 2013
Filename : slotmachine_v1.py
Version : 1.0
'''

#Adapted from "nesting.py" found in Lesson 05 code

class MyApp:
    def __init__(self, parent):

        self.myParent = parent
        
        #Our topmost frame is called slotContainer
        self.slotContainer = Frame(parent)
        self.slotContainer.pack()

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
        
        # buttons frame
        self.buttons_frame = Frame(self.slotContainer) ###
        self.buttons_frame.pack(
            side=BOTTOM, ###
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            padx=buttons_frame_padx,
            pady=buttons_frame_pady,
            )

        # top frame
        self.top_frame = Frame(self.slotContainer)
        self.top_frame.pack(side=TOP,
            fill=BOTH,
            expand=YES,
            )
        
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

        #right_frame
        #self.right_frame = Frame(self.top_frame, background="tan",
            #borderwidth=5, relief=RIDGE,
            #width=800,
            #)

        #self.right_frame.pack(side=RIGHT,
            #fill=BOTH,
            #expand=YES,
            #)
        
        # now we add the buttons to the buttons_frame
        self.button1 = Button(self.buttons_frame, command=self.button1Click)
        self.button1.configure(text="Bet $50", background= "grey")
        self.button1.focus_force()
        self.button1.configure(
            width=button_width, 
            padx=button_padx, 
            pady=button_pady 
            )

        self.button1.pack(side=LEFT)
        self.button1.bind("<Return>", self.button1Click_a)
        
        self.button2 = Button(self.buttons_frame, command=self.button2Click)
        self.button2.configure(text="Bet $100", background="grey")
        self.button2.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady 
            )

        self.button2.pack(side=LEFT)
        self.button2.bind("<Return>", self.button2Click_a)
        
        self.button3 = Button(self.buttons_frame, command=self.button3Click)
        self.button3.configure(text="Bet $500", background="grey")
        self.button3.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
           )
        
        self.button3.pack(side=LEFT)
        self.button3.bind("<Return>", self.button3Click_a)
        
        self.button4 = Button(self.buttons_frame, command=self.button4Click)
        self.button4.configure(text="Bet $1000", background="grey")
        self.button4.configure(
            width=button_width,
            padx=button_padx,
            pady=button_pady
           )
        
        self.button4.pack(side=LEFT)
        self.button4.bind("<Return>", self.button4Click_a)
        
        self.button5 = Button(self.buttons_frame, command=self.button5Click)
        self.button5.configure(text="Spin", background="grey")
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
        

    def button1Click(self):
        if self.button1["background"] == "grey":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "grey"
            
    def button2Click(self):
        if self.button2["background"] == "grey":
            self.button2["background"] = "yellow"
        else:
            self.button2["background"] = "grey"
        
    def button3Click(self):
        if self.button3["background"] == "grey":
            self.button3["background"] = "yellow"
            #label1.text= "Hello World"
        else:
            self.button3["background"] = "grey"
            
    def button4Click(self):
        if self.button4["background"] == "grey":
            self.button4["background"] = "yellow"
        else:
            self.button4["background"] = "grey"
            
    def button5Click(self):
        if self.button5["background"] == "grey":
            self.button5["background"] = "yellow"
        else:
            self.button5["background"] = "grey"

    def button6Click(self):
        self.myParent.destroy()

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

def main():
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()

if __name__ == "__main__": main()