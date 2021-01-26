import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 200)
        self.setWindowTitle('Мини-калькулятор')

        self.lbl1 = QLabel(self)
        self.lbl1.setText('Первое число(целое):')
        self.lbl1.move(0, 0)

        self.name_input1 = QLineEdit(self)
        self.name_input1.move(0, 20)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(0, 180)

        self.lbl2 = QLabel(self)
        self.lbl2.setText('Второе число(целое):')
        self.lbl2.move(0, 160)

        self.btn = QPushButton(self)
        self.btn.move(150, 80)
        self.btn.resize(100, 40)
        self.btn.setText('-->')
        self.btn.clicked.connect(self.btn_pushed)

        self.lbl3 = QLabel(self)
        self.lbl3.move(300, 0)
        self.lbl3.setText('Сумма:')

        self.lbl4 = QLabel(self)
        self.lbl4.move(300, 50)
        self.lbl4.setText('Разность:')


        self.lbl5 = QLabel(self)
        self.lbl5.move(300, 100)
        self.lbl5.setText('Произведение:')


        self.lbl6 = QLabel(self)
        self.lbl6.move(300, 150)
        self.lbl6.setText('Частное:')

        self.lcd1 = QLCDNumber(self)
        self.lcd1.move(450, 0)
        self.lcd1.resize(100, 40)

        self.lcd2 = QLCDNumber(self)
        self.lcd2.move(450, 50)
        self.lcd2.resize(100, 40)


        self.lcd3 = QLCDNumber(self)
        self.lcd3.move(450, 100)
        self.lcd3.resize(100, 40)

        self.lcd4 = QLCDNumber(self)
        self.lcd4.move(450, 150)
        self.lcd4.resize(100, 40)

    def btn_pushed(self):
        first = int(self.name_input1.text())
        second = int(self.name_input2.text())
        print(first + second)
        print(first - second)
        print(first * second)
        self.lcd1.display(first + second)
        self.lcd2.display(first - second)
        self.lcd3.display(first * second)
        if second == 0:
            self.lcd4.display('Error')
        else:
            self.lcd4.display(first // second)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
