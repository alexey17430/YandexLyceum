import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.box1 = QCheckBox(self)
        self.box1.move(25, 25)
        self.box1.setText('Чизбургер')

        self.box2 = QCheckBox(self)
        self.box2.move(25, 50)
        self.box2.setText('Гамбургер')

        self.box3 = QCheckBox(self)
        self.box3.move(25, 75)
        self.box3.setText('Кока-кола')

        self.box4 = QCheckBox(self)
        self.box4.move(25, 100)
        self.box4.setText('Фанта')

        self.box5 = QCheckBox(self)
        self.box5.move(25, 125)
        self.box5.setText('Нагетсы')

        self.box6 = QCheckBox(self)
        self.box6.move(25, 150)
        self.box6.setText('Картошка фри')

        self.box7 = QCheckBox(self)
        self.box7.move(25, 175)
        self.box7.setText('Пирожок')

        self.btn = QPushButton(self)
        self.btn.move(25, 200)
        self.btn.resize(100, 40)
        self.btn.setText('Заказать')
        self.btn.clicked.connect(self.btn_pushed)

        self.menu = QPlainTextEdit(self)
        self.menu.move(25, 250)
        self.menu.resize(200, 100)

    def btn_pushed(self):
        sp_menu = ['Ваш заказ:']
        for i in range(1, 8):
            if eval(f'bool(self.box{i}.checkState())'):
                sp_menu.append(eval(f'self.box{i}.text()'))
        for i in range(len(sp_menu)):
            if i != 0:
                sp_menu[i] = f'{i}) ' + sp_menu[i]
        self.menu.setPlainText('\n'.join(sp_menu))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
