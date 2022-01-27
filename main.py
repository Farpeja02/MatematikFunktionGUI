# importing tkinter module
from tkinter import *
from tkinter.ttk import *
from SaveFile import Save
from MFfile import listWindowClass

class mainWindow:
    def __init__(self):
        # creating tkinter window
        self.root = Tk()
        self.root.protocol('WM_DELETE_WINDOW',self.callback)

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)


        self.add = Entry(self.root)
        self.add.pack()

        self.runButton = Button(self.root, text="Run", command=lambda: listWindowClass(self,self.add.get()))
        self.runButton.pack(padx = 20, pady = 10,side=LEFT)

        self.saveButton = Button(self.root, text="Save", command= Save)
        self.saveButton.pack(padx = 20, pady = 10,side=LEFT)


        # infinite loop
        mainloop()


    def callback(self):
        self.root.destroy()
        print("hej")

if __name__ == '__main__':

    main = mainWindow()


