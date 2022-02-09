from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import sympy as sym
from tkinter.ttk import *
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import matplotlib.pyplot as plt


class listWindowClass:
    def __init__(self, master,input):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")
        self.input = input
        Label(self.listWindow, text="Liste over indbetalinger.. eller.. noget der ligner en cylinder").pack()



        self.plot()

    def plot(self):
        fig, ax = plt.subplots()


        self.input = self.input.split('=')[1]

        x, y = sym.symbols('x y')

        expr = parse_expr(self.input)

        f = sym.lambdify([x], expr)

        X = np.arange(-200, 100, 1)
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




