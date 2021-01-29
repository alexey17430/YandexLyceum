import sys
from PyQt5.QtWidgets import QApplication, QRadioButton, QLabel, QPlainTextEdit, QListWidgetItem
from PyQt5.QtWidgets import QMainWindow, QButtonGroup, QPushButton
from PyQt5 import QtGui, uic

# константа с матрицей
MATRICA = [[1, 0, 0, 1, 1, 1, 0, 1],
           [1, 0, 0, 1, 1, 0, 0, 1],
           [1, 0, 0, 1, 1, 1, 0, 1],
           [1, 1, 0, 1, 1, 1, 0, 1],
           [1, 0, 0, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 1, 1, 1, 1],
           [1, 0, 1, 1, 0, 1, 0, 1],
           [1, 0, 1, 1, 0, 1, 0, 1]]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Widget Art')
        self.setGeometry(500, 300, 500, 500)
        self.font1 = QtGui.QFont()
        self.font1.setPointSize(18)
        self.font2 = QtGui.QFont()
        self.font2.setPointSize(12)
        self.font3 = QtGui.QFont()
        self.font3.setPointSize(10)
        btn_size = 500 / len(MATRICA)
        x, y = 0, 0
        for line in MATRICA:
            for elem in line:
                btn = QPushButton(self)
                btn.resize(btn_size, btn_size)
                btn.move(x, y)
                x += btn_size
                print(x)
                if int(elem) == 1:
                    btn.setStyleSheet('QPushButton {background-color: red; color: red;}')
                else:
                    btn.setStyleSheet('QPushButton {background-color: green; color: green;}')
            x = 0
            y += btn_size


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
