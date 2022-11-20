import math
from math import sin, cos
import sys
import copy

import numpy as np
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

from DFT import DFT, DFT_numpy, DFT_original, DFT_trigonometric
from numpy import allclose


class MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setWindowTitle("DFT")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.formula_text = QLineEdit()
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.formula_text)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        signal_length = 8
        period = 2 * math.pi / 3

        formula = lambda a: 2 * sin(6*a) + 3 * cos(3*a)

        x = [[]]
        for i in range(signal_length):
            x[0].append(formula(period / signal_length * i))
        dots_count = len(x[0])

        X1 = DFT(copy.deepcopy(x))
        X2 = np.fft.fft(copy.deepcopy(x[0]))
        print(allclose(X1, X2))

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar([str(x) for x in range(dots_count)], X1, zorder=2)
        plt.xticks([0, (dots_count - 1) // 5, (dots_count - 1) // 5 * 2, (dots_count - 1) // 5 * 3, (dots_count - 1) // 5 * 4, dots_count - 1])
        plt.grid(zorder=1)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
