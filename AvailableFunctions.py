from Function import Function
from math import sin, cos, pi


class AvailableFunctions:
    functions = {'2 * sin(4 * x) + 3 * cos(2 * x)':
                     Function(lambda x: 2 * sin(4 * x) + 3 * cos(2 * x), pi),
                 'sin(10 * 2 * pi * x) + 0.5 * sin(5 * 2 * pi * x)':
                     Function(lambda x: sin(10 * 2 * pi * x) + 0.5 * sin(5 * 2 * pi * x), 0.2),
                 '5 * sin(4 * x) + 6 * cos(3 * x) + sin(5 * x)':
                     Function(lambda x: 5 * sin(4 * x) + 6 * cos(3 * x) + sin(5 * x), 2 * pi),
                 'sin^4(x)':
                     Function(lambda x: (sin(x))**4, pi)
                 }
