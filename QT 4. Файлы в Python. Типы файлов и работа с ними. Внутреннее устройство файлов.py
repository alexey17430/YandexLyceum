import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit
from PyQt5 import QtGui


def random_line():
    file = open('lines.txt')
    sp = list(map(lambda st: st.strip(), file.readlines()))
    if len(sp) > 0:
        return random.choice(sp)
    file.close()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 400, 100)
        self.setWindowTitle('Cлучайная строка из файла - 2')
        self.btn_font = QtGui.QFont()
        self.btn_font.setPointSize(16)
        self.line_font = QtGui.QFont()
        self.line_font.setPointSize(12)

        self.btn = QPushButton(self)
        self.btn.move(20, 20)
        self.btn.resize(100, 60)
        self.btn.setText('Получить')
        self.btn.setFont(self.btn_font)
        self.btn.clicked.connect(self.btn_pushed)

        self.line = QPlainTextEdit(self)
        self.line.resize(240, 60)
        self.line.move(140, 20)
        self.line.setFont(self.line_font)

    def btn_pushed(self):
        self.line.setPlainText(random_line())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
