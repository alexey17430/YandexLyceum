# имя файла со строками текста input.txt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit
from PyQt5 import QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 350, 350)
        self.setWindowTitle('Перемешивание')
        self.font = QtGui.QFont()
        self.font.setPointSize(14)

        self.btn = QPushButton(self)
        self.btn.resize(200, 50)
        self.btn.move(25, 25)
        self.btn.setText('Загрузить строки')
        self.btn.setFont(self.font)
        self.btn.clicked.connect(self.button_pushed)

        self.edit = QPlainTextEdit(self)
        self.edit.move(25, 100)
        self.edit.resize(300, 225)
        self.edit.setFont(self.font)

    def button_pushed(self):
        file = open('input.txt')
        lines = file.readlines()
        for i in range(1, len(lines), 2):
            self.edit.setPlainText(self.edit.toPlainText() + lines[i])
        self.edit.setPlainText(self.edit.toPlainText() + '\n')
        for i in range(0, len(lines), 2):
            self.edit.setPlainText(self.edit.toPlainText() + lines[i])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
