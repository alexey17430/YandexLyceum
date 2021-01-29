import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber
from math import factorial


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        for i in range(10):
            eval(f'self.btn{i}.clicked.connect(self.num_pushed)')
        self.btn_clear.clicked.connect(self.btn_clear_clicked)
        self.btn_eq.clicked.connect(self.btn_equal)
        self.btn_plus.clicked.connect(self.btn_operation)
        self.btn_minus.clicked.connect(self.btn_operation)
        self.btn_mult.clicked.connect(self.btn_operation)
        self.btn_div.clicked.connect(self.btn_operation)
        self.btn_sqrt.clicked.connect(self.btn_operation)
        self.btn_pow.clicked.connect(self.btn_operation)
        self.btn_fact.clicked.connect(self.btn_operation)
        self.btn_dot.clicked.connect(self.dot_pushed)
        self.dot_used = False

    def btn_clear_clicked(self):
        self.table.display(0)
        self.dot_used = False

    def num_pushed(self):
        number = str(self.sender().text())
        screen_now = str(int(self.table.value()))
        if self.dot_used:
            self.desetich.append(number)
            screen_now += '.'
            for elem in self.desetich:
                screen_now += elem
            self.table.display(screen_now)
            print(self.desetich)
        else:
            self.table.display(int(screen_now + number))

    def dot_pushed(self):
        self.dot_used = True
        self.desetich = list()

    def btn_operation(self):
        self.first_number = self.table.value()
        self.operation = self.sender().text()
        if self.operation == '!':
            self.table.display(factorial(self.first_number))
        elif self.operation == '√':
            self.table.display(self.first_number ** 0.5)
        else:
            self.table.display(0)
        self.dot_used = False

    def btn_equal(self):
        n = self.table.value()
        if self.operation == '^':
            self.table.display(self.first_number ** n)
        else:
            result = eval(str(self.first_number) + self.operation + str(n))
            self.table.display(result)
        self.dot_used = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
