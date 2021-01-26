import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.box1 = QCheckBox(self)
        self.box1.move(25, 25)
        self.box1.setText('Чизбургер')
        self.box1.clicked.connect(self.box_pushed)
        self.box1.setAccessibleName('box1')

        self.box2 = QCheckBox(self)
        self.box2.move(25, 50)
        self.box2.setText('Гамбургер')
        self.box2.clicked.connect(self.box_pushed)
        self.box2.setAccessibleName('box2')

        self.box3 = QCheckBox(self)
        self.box3.move(25, 75)
        self.box3.setText('Кока-кола')
        self.box3.clicked.connect(self.box_pushed)
        self.box3.setAccessibleName('box3')

        self.box4 = QCheckBox(self)
        self.box4.move(25, 100)
        self.box4.setText('Фанта')
        self.box4.clicked.connect(self.box_pushed)
        self.box4.setAccessibleName('box4')

        self.box5 = QCheckBox(self)
        self.box5.move(25, 125)
        self.box5.setText('Нагетсы')
        self.box5.clicked.connect(self.box_pushed)
        self.box5.setAccessibleName('box5')

        self.box6 = QCheckBox(self)
        self.box6.move(25, 150)
        self.box6.setText('Картошка фри')
        self.box6.clicked.connect(self.box_pushed)
        self.box6.setAccessibleName('box6')

        self.box7 = QCheckBox(self)
        self.box7.move(25, 175)
        self.box7.setText('Пирожок')
        self.box7.clicked.connect(self.box_pushed)
        self.box7.setAccessibleName('box7')

        self.btn = QPushButton(self)
        self.btn.move(25, 200)
        self.btn.resize(100, 40)
        self.btn.setText('Заказать')
        self.btn.clicked.connect(self.btn_pushed)

        self.menu = QPlainTextEdit(self)
        self.menu.move(25, 250)
        self.menu.resize(225, 100)

        self.line1 = QLineEdit(self)
        self.line1.move(150, 25)
        self.line1.resize(100, 20)
        self.line1.setText('0')
        self.line1.setDisabled(True)

        self.line2 = QLineEdit(self)
        self.line2.move(150, 50)
        self.line2.resize(100, 20)
        self.line2.setText('0')
        self.line2.setDisabled(True)

        self.line3 = QLineEdit(self)
        self.line3.move(150, 75)
        self.line3.resize(100, 20)
        self.line3.setText('0')
        self.line3.setDisabled(True)

        self.line4 = QLineEdit(self)
        self.line4.move(150, 100)
        self.line4.resize(100, 20)
        self.line4.setText('0')
        self.line4.setDisabled(True)

        self.line5 = QLineEdit(self)
        self.line5.move(150, 125)
        self.line5.resize(100, 20)
        self.line5.setText('0')
        self.line5.setDisabled(True)

        self.line6 = QLineEdit(self)
        self.line6.move(150, 150)
        self.line6.resize(100, 20)
        self.line6.setText('0')
        self.line6.setDisabled(True)

        self.line7 = QLineEdit(self)
        self.line7.move(150, 175)
        self.line7.resize(100, 20)
        self.line7.setText('0')
        self.line7.setDisabled(not bool(self.box7.checkState()))

    def btn_pushed(self):
        sp_menu = ['Ваш заказ:']  # все товары по 50 рублей
        itogo = 0
        for i in range(1, 8):
            if eval(f'bool(self.box{i}.checkState())'):
                tovar = eval(f"self.box{i}.text()")
                colvo = eval(f"self.line{i}.text()")
                sp_menu.append(f'Товар: {tovar}, количество: {int(colvo)},'
                               f' сумма: {int(colvo) * 50}')
                itogo += int(colvo) * 50
        sp_menu.append(f'\nИтого: {itogo}')
        for i in range(len(sp_menu)):
            if i != 0 and i + 1 != len(sp_menu):
                sp_menu[i] = f'{i}) ' + sp_menu[i]
        self.menu.setPlainText('\n'.join(sp_menu))

    def box_pushed(self):
        box_name = self.sender().accessibleName()
        if eval(f'self.{box_name}.checkState()'):
            eval(f'self.line{box_name[-1]}.setText("1")')
        eval(f'self.line{box_name[-1]}.setDisabled(not self.{box_name}.checkState())')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
