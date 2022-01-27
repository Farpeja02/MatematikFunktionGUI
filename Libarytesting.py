import matplotlib.pyplot as plt
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot
input = 'y = x**2'



user_input = 'x**2'
y = parse_expr(user_input)

fig = plot(y)


X = np.array(x) #Puts the data into a np array.
Y = np.array(y)
plt.title("The temperature in Sweden on the first of June from 1744 -> 2013") #Title for the plot
plt.xlabel("Year") #Title for the X axis
plt.ylabel("Temperature in celsius") #Title for the Y axis
plt.plot(X,Y) #Plots the data
plt.show() #Creates the png of the plot

# show the plot
plt.show()