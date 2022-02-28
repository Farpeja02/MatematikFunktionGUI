# importing tkinter module
from tkinter import *
from tkinter.ttk import *
#from SaveFile import Save
from MFfile import listWindowClass
from tkinter import messagebox


class mainWindow:
    def __init__(self):
        # creating tkinter window
        self.root = Tk()
        self.root.protocol('WM_DELETE_WINDOW',self.callback)

        self.hasItBeenSaved = 0




        velkomst = Label(self.root, text="Velkommen til Matematisk funktions maskinen")
        velkomst.pack(pady=10)

        guide = Label(self.root, text="Skriv en funktion her og få den vist. Eksempel: y = x + 5")
        guide.pack(pady=10)

        self.add = Entry(self.root)
        self.add.pack()

        evalX = Label(self.root, text="Evaualte from specefic x value, if it's left empty it will be ignored.")
        evalX.pack(pady=10)
        self.addEvalX = Entry(self.root)
        self.addEvalX.pack()




        self.runButton = Button(self.root, text="Run", command=lambda: listWindowClass(self,self.add.get(),self.addLimitValA.get(),self.addLimitValB.get(),self.interval.get(),self.addEvalX.get()))
        self.runButton.pack(padx = 20, pady = 10,side=LEFT)






        limitValA = Label(self.root, text="Limit Value A, Default is -100")
        limitValA.pack(pady=10)
        self.addLimitValA = Entry(self.root)
        self.addLimitValA.pack()

        limitValB = Label(self.root, text="Limit Value B, Default is 100")
        limitValB.pack(pady=10)
        self.addLimitValB = Entry(self.root)
        self.addLimitValB.pack()


        interval = Label(self.root, text="Choose your Interval, Default is 1")
        interval.pack(pady=5)
        self.interval = Entry(self.root)
        self.interval.pack(pady=5, padx =5)


        # infinite loop
        mainloop()


    def callback(self):

        print("hej")

        if self.hasItBeenSaved == 0:
            if messagebox.askyesno("Warning: You're about to close without saving.",
                                                "Would you like to save before closing the program?"):
                self.root.destroy()

            else:
                pass

        if self.hasItBeenSaved == 1:
            self.root.destroy()

    def saveYes(self):
        self.hasItBeenSaved = 1
        print(self.hasItBeenSaved)

    def saveNo(self):
        self.hasItBeenSaved = 0
        print(self.hasItBeenSaved)









if __name__ == '__main__':

    main = mainWindow()
