import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit
from PyQt5 import QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 300, 300)
        self.setWindowTitle('Ним наносит ответный удар')
        self.font = QtGui.QFont()
        self.font.setPointSize(20)
        self.super_font = QtGui.QFont()
        self.super_font.setPointSize(14)
        screen_font = QtGui.QFont()
        screen_font.setPointSize(10)

        x = randint(1, 50)
        y = randint(1, x)
        while True:
            z = randint(1, x)
            if z != y != x:
                break

        self.btn_plus = QPushButton(self)
        self.btn_plus.move(25, 100)
        self.btn_plus.resize(100, 40)
        self.btn_plus.setText(f'+{y}')
        self.btn_plus.setFont(self.font)
        self.btn_plus.clicked.connect(self.btn_pushed)

        self.btn_minus = QPushButton(self)
        self.btn_minus.move(175, 100)
        self.btn_minus.resize(100, 40)
        self.btn_minus.setText(f'-{z}')
        self.btn_minus.setFont(self.font)
        self.btn_minus.clicked.connect(self.btn_pushed)

        self.btn_new_game = QPushButton(self)
        self.btn_new_game.move(75, 150)
        self.btn_new_game.resize(150, 50)
        self.btn_new_game.setText('Начать\nновую игру')
        self.btn_new_game.setFont(self.super_font)
        self.btn_new_game.clicked.connect(self.new_game_pushed)

        self.title_moves = QLabel(self)
        self.title_moves.move(25, 200)
        self.title_moves.setFont(screen_font)
        self.title_moves.resize(100, 40)
        self.title_moves.setText('Осталось ходов')

        self.number_now = QLabel(self)
        self.number_now.move(25, 250)
        self.number_now.setFont(screen_font)
        self.number_now.resize(100, 40)
        self.number_now.setText('Текущее число')

        self.lcd_moves = QLCDNumber(self)
        self.lcd_moves.move(175, 200)
        self.lcd_moves.resize(100, 40)
        self.lcd_moves.display(10)

        self.lcd_number = QLCDNumber(self)
        self.lcd_number.move(175, 250)
        self.lcd_number.resize(100, 40)
        self.lcd_number.display(str(x))

        self.lbl = QLabel(self)
        self.lbl.move(25, 25)
        self.lbl.resize(300, 50)
        self.lbl.setFont(self.super_font)

    def btn_pushed(self):
        number = int(self.sender().text())
        anser = int(self.lcd_number.value())
        self.lcd_moves.display(int(self.lcd_moves.value()) - 1)
        anser += number
        self.lcd_number.display(anser)
        if int(self.lcd_number.value()) == 0:
            self.lbl.setText('Победа, победа - время обеда')
            self.btn_minus.setDisabled(True)
            self.btn_plus.setDisabled(True)
        elif int(self.lcd_moves.value()) == 0:
            self.lbl.setText('Увы и ах, вы проиграли')
            self.btn_minus.setDisabled(True)
            self.btn_plus.setDisabled(True)

    def new_game_pushed(self):
        x = randint(1, 50)
        y = randint(1, x)
        while True:
            z = randint(1, x)
            if z != y != x:
                break

        self.btn_plus.setText(f'+{y}')
        self.btn_minus.setText(f'-{z}')
        self.lcd_moves.display(10)
        self.lcd_number.display(str(x))
        self.btn_minus.setDisabled(False)
        self.btn_plus.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
