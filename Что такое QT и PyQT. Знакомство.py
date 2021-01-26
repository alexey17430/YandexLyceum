import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit
from PyQt5 import QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 475)
        self.setWindowTitle('Калькулятор')
        font = QtGui.QFont()
        font.setPointSize(16)
        screen_font = QtGui.QFont()
        screen_font.setPointSize(30)

        self.btn_dot = QPushButton(self)
        self.btn_dot.resize(75, 75)
        self.btn_dot.move(0, 400)
        self.btn_dot.setText('.')
        self.btn_dot.setFont(font)
        self.btn_dot.clicked.connect(self.num_pushed)

        self.btn_abs = QPushButton(self)
        self.btn_abs.resize(75, 75)
        self.btn_abs.move(75, 400)
        self.btn_abs.setText('±')
        self.btn_abs.setFont(font)
        self.btn_abs.clicked.connect(self.btn_pushed)

        self.btn_eq = QPushButton(self)
        self.btn_eq.resize(150, 75)
        self.btn_eq.move(150, 400)
        self.btn_eq.setText('=')
        self.btn_eq.setFont(font)
        self.btn_eq.setFont(font)
        self.btn_eq.clicked.connect(self.btn_pushed)

        self.btn_plus = QPushButton(self)
        self.btn_plus.resize(75, 75)
        self.btn_plus.move(225, 325)
        self.btn_plus.setText('+')
        self.btn_plus.setFont(font)
        self.btn_plus.clicked.connect(self.btn_pushed)

        self.btn_minus = QPushButton(self)
        self.btn_minus.resize(75, 75)
        self.btn_minus.move(225, 250)
        self.btn_minus.setText('-')
        self.btn_minus.setFont(font)
        self.btn_minus.clicked.connect(self.btn_pushed)

        self.btn_proiz = QPushButton(self)
        self.btn_proiz.resize(75, 75)
        self.btn_proiz.move(225, 175)
        self.btn_proiz.setText('*')
        self.btn_proiz.setFont(font)
        self.btn_proiz.clicked.connect(self.btn_pushed)

        self.btn_chast = QPushButton(self)
        self.btn_chast.resize(75, 75)
        self.btn_chast.move(225, 100)
        self.btn_chast.setText('/')
        self.btn_chast.setFont(font)
        self.btn_chast.clicked.connect(self.btn_pushed)

        poz = 0
        number = ['C', '0', 'CE'] + list(str(i) for i in range(1, 10))
        for deltay in (0, -75, -150, -225):
            for deltax in (0, 75, 150):
                self.btn_num = QPushButton(self)
                self.btn_num.resize(75, 75)
                self.btn_num.move(deltax, 325 + deltay)
                self.btn_num.setText(number[poz])
                self.btn_num.setFont(font)
                if self.btn_num.text() in 'CE':
                    self.btn_num.clicked.connect(self.btn_pushed)
                else:
                    self.btn_num.clicked.connect(self.num_pushed)
                poz += 1

        self.screen = QLabel(self)
        self.screen.move(0, 25)
        self.screen.resize(300, 75)
        self.screen.setText('')  # предел - 13 символов
        self.screen.setFont(screen_font)

        self.small_screen = QLabel(self)
        self.small_screen.move(0, 0)
        self.small_screen.resize(300, 25)
        self.small_screen.setText('')
        self.screen.setFont(font)

    def num_pushed(self):
        # 13 - максимальное количесиво цифр
        number = self.sender().text()
        screen_now = self.screen.text()
        if (number == '.' and '.' in screen_now) or len(screen_now) == 13:
            pass
        else:
            self.screen.setText(screen_now + number)

    def btn_pushed(self):
        deyst = self.sender().text()
        if '=' == deyst:
            small_screen = self.small_screen.text()
            screen = self.screen.text()
            if '/' in small_screen and screen == '0':
                self.screen.setText('Деление на ноль')
            else:
                ans = eval(small_screen + screen)
                self.small_screen.setText('')
                self.screen.setText(str(ans))
        elif deyst in '+-*/':
            self.small_screen.setText(self.screen.text() + deyst)
            self.screen.setText('')
        elif deyst == '±':
            if len(self.small_screen.text()) == 0:
                self.screen.setText(abs(int(self.screen.text())))
            else:
                self.screen.setText(abs(int(eval(self.small_screen.text() + self.screen.text()))))
        elif deyst in 'С':
            self.screen.setText('')
            self.small_screen.setText('')
        else:
            self.screen.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
