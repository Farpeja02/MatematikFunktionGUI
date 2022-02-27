from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import sympy as sym
from tkinter.ttk import *
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from tkinter.filedialog import asksaveasfile

class listWindowClass:
    def __init__(self, master,input,limitA,limitB,interval):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")
        self.input = input
        self.limitA = limitA
        if self.limitA == "":
            self.limitA = -100


        self.limitB = limitB
        if self.limitB == "":
            self.limitB = 100


        self.interval = interval
        if self.interval == "":
            self.interval = 1




        Label(self.listWindow, text="Liste over indbetalinger.. eller.. noget der ligner en cylinder").pack()



        self.plot()


    def plot(self):
        fig, ax = plt.subplots()


        self.input = self.input.split('=')[1]

        x, y = sym.symbols('x y')

        expr = parse_expr(self.input)

        f = sym.lambdify([x], expr)

        X = np.arange(int(self.limitA), int(self.limitB), int(self.interval))
        Y = f(X)
        ax.plot(X, Y)



        canvas = FigureCanvasTkAgg(fig,
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
        
        #file = asksaveasfile(initialfile='Untitled.png', defaultextension=".png", filetypes=[("All Files", "*.*")])
        #fig.savefig(file)

        # gemmer på desktop
        fig.savefig('/users/emiliemunklarsen/Desktop/graph.png')







