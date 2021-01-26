import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 100)
        self.setWindowTitle('Арифмометр')

        self.name_input1 = QLineEdit(self)
        self.name_input1.move(35 + 0, 35)
        self.name_input1.resize(100, 30)
        self.name_input1.setText('0')

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(35 + 220, 35)
        self.name_input2.resize(100, 30)
        self.name_input2.setText('0')


        self.btn1 = QPushButton(self)
        self.btn1.setText('+')
        self.btn1.move(35 + 100, 35)
        self.btn1.resize(40, 30)
        self.btn1.clicked.connect(self.button_pushed)

        self.btn2 = QPushButton(self)
        self.btn2.setText('-')
        self.btn2.move(35 + 140, 35)
        self.btn2.resize(40, 30)
        self.btn2.clicked.connect(self.button_pushed)

        self.btn3 = QPushButton(self)
        self.btn3.setText('*')
        self.btn3.move(35 + 180, 35)
        self.btn3.resize(40, 30)
        self.btn3.clicked.connect(self.button_pushed)

        self.lbl = QLabel(self)
        self.lbl.setText('=')
        self.lbl.move(35 + 321, 42)

        self.name_input3 = QLineEdit(self)
        self.name_input3.move(35 + 330, 35)
        self.name_input3.resize(100, 30)
        self.name_input3.setDisabled(True)

    def button_pushed(self):
        first = str(self.name_input1.text())
        if len(first) == 0:
            first = 0
        else:
            first = int(first)
        second = str(self.name_input2.text())
        if len(second) == 0:
            second = 0
        else:
            second = int(second)
        self.name_input3.setText(str(eval(f'{first} {self.sender().text()} {second}')))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
