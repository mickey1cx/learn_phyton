# https://ru.stackoverflow.com/questions/969590
# run in jupiter notebook

import matplotlib
import numpy
from numpy import linspace
import matplotlib.pyplot as plt

def f1(x):
    value = -x ** 2 + x + 1
    return numpy.nan if value < 0 else value ** 0.5

matplotlib.style.use('ggplot')
%matplotlib inline
x = linspace(-20, 20, 10000)

plt.axis([-20, 20, -20, 20])

y = numpy.tan(x)
y[:-1][numpy.diff(y) < 0] = numpy.nan
plt.plot(x, y, 'r')

y = numpy.array([f1(i) for i in x])
plt.plot(x, y, 'g')

plt.grid()
plt.show()
