from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk


class listWindowClass:
    def __init__(self, master,input):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")
        self.input = input
        Label(self.listWindow, text="Liste over indbetalinger.. eller.. noget der ligner en cylinder").pack()

        MFimg = self.MF()
        MFimg.save('Plot.png')

        img = ImageTk.PhotoImage(file = 'Plot.png')
        panel = Label(self.listWindow, image=img)
        panel.image = img
        panel.pack(side="bottom", fill="both", expand="yes")

    def MF(self):
        #self.input = self.input[2 + self.input.find('='):]
        self.input = self.input.split('=')[1]

        y = parse_expr(self.input)
        fig = plot(y)
        return fig



