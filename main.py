# importing tkinter module
from tkinter import *
from tkinter.ttk import *
#from SaveFile import Save
from MFfile import MFWindowClass
from tkinter import messagebox


class mainWindow: #This is the main window that opens when the program runs
    def __init__(self):
        # creating tkinter window
        self.root = Tk()
        self.root.protocol('WM_DELETE_WINDOW',self.callback) #The 'WM_DELETE_WINDOW' tells the program to run callback when the main window is closed.

        self.hasItBeenSaved = 1 #Variable to check if the program has been saved, starts at one so it doesnt trigger the messagebox before the user click run.




        velkomst = Label(self.root, text="Welcome to the Mathematical function machine!") #Labels to describe the program
        velkomst.pack(pady=10)

        guide = Label(self.root, text="Write a function here, such as: y = x + 5")
        guide.pack(pady=10)

        self.add = Entry(self.root) #Entry for the MFFile
        self.add.pack()

        evalX = Label(self.root, text="Evaualte from specefic x value, if it's left empty it will be ignored.") #The given X value for the Eval
        evalX.pack(pady=10,padx = 20)
        self.addEvalX = Entry(self.root)
        self.addEvalX.pack()



        #Runs the MFWindowClass with all the values given from other entries.
        self.runButton = Button(self.root, text="Run", command=lambda: MFWindowClass(self, self.add.get(), self.addLimitValA.get(), self.addLimitValB.get(), self.interval.get(), self.addEvalX.get()))
        self.runButton.pack(padx = 70, pady = 10,side=LEFT)





        #These 3 give strings that are used to describe the limit values and intervals.
        limitValA = Label(self.root, text="Limit Value A, Default is -100")
        limitValA.pack(pady=10)
        self.addLimitValA = Entry(self.root)
        self.addLimitValA.pack()

        limitValB = Label(self.root, text="Limit Value B, Default is 100")
        limitValB.pack(pady=10)
        self.addLimitValB = Entry(self.root)
        self.addLimitValB.pack()


        interval = Label(self.root, text="Choose your Interval, Default is 1")
        interval.pack(pady=5,padx=10)
        self.interval = Entry(self.root)
        self.interval.pack(pady=5, padx =5)


        # infinite loop
        mainloop()


    def callback(self): #This runs when the program is closed, it opens a messagebox if the user has not saved yet.

        if self.hasItBeenSaved == 0:
            if messagebox.askyesno("Warning: You're about to close without saving.",
                                                "Are you sure you want to close the program?"):
                self.root.destroy()

            else:
                pass

        if self.hasItBeenSaved == 1:
            self.root.destroy()



    #These methods tell the program if the user has saved.
    def saveYes(self):
        self.hasItBeenSaved = 1

    def saveNo(self):
        self.hasItBeenSaved = 0



if __name__ == '__main__': #Checks the name of the file, and runs it if it fits.

    main = mainWindow()
