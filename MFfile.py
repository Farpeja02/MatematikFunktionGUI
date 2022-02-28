from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import sympy as sym
from tkinter.ttk import *
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from tkinter.filedialog import asksaveasfile


class listWindowClass:
    def __init__(self, master,input,limitA,limitB,interval,evalX):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")
        self.input = input
        self.limitA = limitA
        self.evalX = evalX
        if self.limitA == "":
            self.limitA = -100


        self.limitB = limitB
        if self.limitB == "":
            self.limitB = 100


        self.interval = interval
        if self.interval == "":
            self.interval = 1

        self.input = self.input.split('=')[1]

        Label(self.listWindow, text="Her er din graf :)").pack()


        self.plot()


        self.saveButton = Button(self.listWindow, text="Save", command= self.save)
        self.saveButton.pack(padx = 20, pady = 10,side=LEFT)

        self.evaluator()

    def plot(self):
        self.fig, ax = plt.subplots()
        self.master.saveNo()




        x, y = sym.symbols('x y')

        expr = parse_expr(self.input)

        self.f = sym.lambdify([x], expr)

        X = np.arange(int(self.limitA), int(self.limitB), int(self.interval))
        Y = self.f(X)
        ax.plot(X, Y)



        canvas = FigureCanvasTkAgg(self.fig,
                                   master=self.listWindow)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                       self.listWindow)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

    def evaluator(self):
        if self.evalX != '':
            x  = int(self.evalX)

            y=self.f(x)
            Label(self.listWindow, text=f"The chosen X value is: {y}").pack()
        
    def save(self):
        self.master.saveYes()
        filename = asksaveasfile(initialfile='Untitled.png', defaultextension=".png", filetypes=[("All Files", "*.*")])
        print(filename.name)
        self.fig.savefig(filename.name)









