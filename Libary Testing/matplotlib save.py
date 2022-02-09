from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import matplotlib.pyplot as plt


# plot function is created for
# plotting the graph in
# tkinter window
def plot():

    fig, ax = plt.subplots()

    # list of squares
    X = range(101)
    Y = [xes ** 2 for xes in X]
    ax.plot(X, Y)

#    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
  #         title='About as simple as it gets, folks')
#    ax.grid()
 # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


# the main Tkinter window
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("500x500")

# button that displays the plot
plot_button = Button(master=window,
                     command=plot,
                     height=2,
                     width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

# run the gui
window.mainloop()