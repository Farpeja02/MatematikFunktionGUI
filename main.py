# importing tkinter module
from tkinter import *
from tkinter.ttk import *
from MFfile import MF
from SaveFile import Save


class mainWindow:
    def __init__(self):
        # creating tkinter window
        self.root = Tk()

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)


        self.add = Entry(self.root)
        self.add.pack()

        self.runButton = Button(self.root, text="Run", command= MF())
        self.runButton.pack(padx = 20, pady = 10,side=LEFT)

        self.saveButton = Button(self.root, text="Save", command= Save())
        self.saveButton.pack(padx = 20, pady = 10,side=LEFT)


        # infinite loop
        mainloop()




if __name__ == '__main__':

    main = mainWindow()

    print("hej")
