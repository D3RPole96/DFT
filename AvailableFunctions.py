from Function import Function
from math import sin, cos, pi


class AvailableFunctions:
    functions = {'2 * sin(4 * x) + 3 * cos(2 * x) + 0.5 * cos(20 * x)':
                     Function(lambda x: 2 * sin(4 * x) + 3 * cos(2 * x) + 0.5 * cos(20 * x), pi),
                 '5 * sin(4 * x) + 6 * cos(3 * x) + sin(5 * x)':
                     Function(lambda x: 5 * sin(4 * x) + 6 * cos(3 * x) + sin(5 * x), 2 * pi),
                 'sin^4(x)':
                     Function(lambda x: (sin(x))**4, pi),
                 'sin^7(x) + cos^3(x)':
                     Function(lambda x: (sin(x)) ** 7 + (cos(x)) ** 3, 2*pi)
                 }
