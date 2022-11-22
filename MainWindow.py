import sys

import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QLineEdit, QHBoxLayout, QCheckBox, \
    QRadioButton, QMessageBox, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from AvailableFunctions import AvailableFunctions


class MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setWindowTitle("DFT")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.checkboxes = {}
        for key in AvailableFunctions.functions:
            self.checkboxes[key] = QCheckBox(key, self)
            self.checkboxes[key].setFixedHeight(18)

        self.dtf_button = QPushButton('DFT')
        self.idtf_button = QPushButton('IDFT')
        self.dtf_button.clicked.connect(self.draw_dft)
        self.idtf_button.clicked.connect(self.draw_idft)

        layout = QVBoxLayout()
        buttons = QHBoxLayout()
        middle = QHBoxLayout()
        bottom_layout = QHBoxLayout()
        checkboxes_layout = QVBoxLayout()

        empty_text = QLabel()
        empty_text.setFixedHeight(10)
        checkboxes_layout.addWidget(empty_text)

        layout.addWidget(self.toolbar)

        layout.addWidget(self.canvas)
        for _, v in self.checkboxes.items():
            checkboxes_layout.addWidget(v)
        bottom_layout.addLayout(checkboxes_layout)

        text = QLabel('Количество периодов функции:')
        self.periods_layout = QVBoxLayout()
        text.setFixedHeight(10)
        text.setAlignment(Qt.AlignBottom)
        self.periods_layout.addWidget(text)

        self.periods_count_list = {}
        for name, function in AvailableFunctions.functions.items():
            periods_count = QLineEdit('1')
            periods_count.setFixedWidth(200)
            periods_count.setFixedHeight(18)
            self.periods_count_list[name] = periods_count
            self.periods_layout.addWidget(periods_count)

        bottom_layout.addLayout(self.periods_layout)

        middle.addLayout(bottom_layout)
        layout.addLayout(middle)

        buttons.addWidget(self.dtf_button)
        buttons.addWidget(self.idtf_button)

        layout.addLayout(buttons)

        self.setLayout(layout)

    def draw_dft(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        colors = ['m', 'r', 'g', 'b']
        thin = [0.3, 0.2, 0.1]
        zorder = [2, 3, 4, 5]

        names = []
        functions_DFT = []
        x_axises = []
        max_axis = -1e-9

        checkboxed_functions_count = 0

        for name, function in AvailableFunctions.functions.items():
            if self.checkboxes[name].isChecked():
                checkboxed_functions_count += 1

        if checkboxed_functions_count > 1:
            self.showDialog("При прямом преобразовании пока нельзя выбирать больше одной функции")
            return

        for name, function in AvailableFunctions.functions.items():
            if not self.checkboxes[name].isChecked():
                continue

            names.append(name)

            function_DFT = function.get_DFT(64)
            functions_DFT.append(function_DFT)

            x_axis = [(x * 1 / function.period) for x in range(len(function_DFT))]
            x_axises.append(x_axis)
            max_axis = max(max_axis, x_axis[-1])

        for i in range(len(names)):
            ax.bar(x_axises[i], functions_DFT[i], 0.05 * (max_axis / 10), zorder=zorder.pop(),
                   color=colors.pop(), label=names[i])
            ax.grid(zorder=1)

            ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

            plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')

            plt.xticks(x_axises[i])

        # ax.legend()

        self.canvas.draw()

    def draw_idft(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        colors = ['m', 'r', 'g', 'b']

        for name, function in AvailableFunctions.functions.items():
            if not self.checkboxes[name].isChecked():
                continue

            periods_count_text = self.periods_count_list[name]

            if not periods_count_text.text().isnumeric() or int(periods_count_text.text()) < 1:
                self.showDialog("Вводимое значение дожно быть целым числом от 1")
                return

            periods_count = int(periods_count_text.text())
            function_IDFT = function.get_IDFT(64) * periods_count

            x_axis = [function.period / (len(function_IDFT) / periods_count) * x for x in range(len(function_IDFT))]

            ax.plot(x_axis, function_IDFT, 0.1, zorder=2, color=colors.pop(), label=name)
            ax.grid(zorder=1)

            ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

            plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')

        #ax.legend()

        self.canvas.draw()

    def showDialog(self, message):
        msgBox = QMessageBox()
        msgBox.setIconPixmap(QIcon("Goose.jpg").pixmap(80, 80))
        msgBox.setText(message)
        msgBox.setWindowTitle("Некорректный ввод")
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
