import sys
from PyQt5.QtWidgets import QApplication, QRadioButton, QLabel
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
from PyQt5 import QtGui, uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('флаги.ui', self)
        self.setWindowTitle('Текстовые флаги')
        self.font1 = QtGui.QFont()
        self.font1.setPointSize(18)
        self.font2 = QtGui.QFont()
        self.font2.setPointSize(12)
        self.font3 = QtGui.QFont()
        self.font3.setPointSize(10)

        self.lbl = QLabel(self)
        self.lbl.move(50, 250)
        self.lbl.resize(275, 50)
        self.lbl.setFont(self.font3)

        self.label.setFont(self.font1)
        self.label_2.setFont(self.font1)
        self.label_3.setFont(self.font1)
        self.pushButton.setFont(self.font2)
        self.pushButton.clicked.connect(self.btn_pushed)

        first_layout = QButtonGroup(self)
        second_layout = QButtonGroup(self)
        third_layout = QButtonGroup(self)

        for i in range(1, 10):
            eval(f'self.radioButton_{i}.setFont(self.font2)')
            if str(i) in '123':
                eval(f'first_layout.addButton(self.radioButton_{i})')
            elif str(i) in '456':
                eval(f'second_layout.addButton(self.radioButton_{i})')
            elif str(i) in '789':
                eval(f'third_layout.addButton(self.radioButton_{i})')
            if i == 1 or i == 4 or i == 7:
                eval(f'self.radioButton_{i}.setChecked(True)')

    def btn_pushed(self):
        flag_colors = list()
        for i in range(1, 4):
            if eval(f'self.radioButton_{i}.isChecked()'):
                eval(f'flag_colors.append(self.radioButton_{i}.text())')
        for i in range(4, 7):
            if eval(f'self.radioButton_{i}.isChecked()'):
                eval(f'flag_colors.append(self.radioButton_{i}.text())')
        for i in range(7, 10):
            if eval(f'self.radioButton_{i}.isChecked()'):
                eval(f'flag_colors.append(self.radioButton_{i}.text())')
        self.lbl.setText(f'Цвета флага: {", ".join(flag_colors)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
