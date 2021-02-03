import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit
from PyQt5 import QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 450, 350)
        self.setWindowTitle('Текстовый редактор')
        self.font = QtGui.QFont()
        self.font.setPointSize(14)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(25, 25)
        self.line_edit.resize(150, 50)
        self.line_edit.setFont(self.font)

        self.btn1 = QPushButton(self)
        self.btn1.move(25, 100)
        self.btn1.resize(150, 50)
        self.btn1.setText('Создать новый')
        self.btn1.setFont(self.font)
        self.btn1.clicked.connect(self.button_pushed1)

        self.btn2 = QPushButton(self)
        self.btn2.move(25, 175)
        self.btn2.resize(150, 50)
        self.btn2.setText('Сохранить файл')
        self.btn2.setFont(self.font)
        self.btn2.clicked.connect(self.button_pushed2)

        self.btn3 = QPushButton(self)
        self.btn3.move(25, 250)
        self.btn3.resize(150, 50)
        self.btn3.setText('Открыть файл')
        self.btn3.setFont(self.font)
        self.btn3.clicked.connect(self.button_pushed3)

        self.bloknot = QPlainTextEdit(self)
        self.bloknot.move(200, 25)
        self.bloknot.resize(225, 275)
        self.bloknot.setFont(self.font)
        self.bloknot.setDisabled(True)

    def button_pushed1(self):
        self.bloknot.setDisabled(False)
        self.bloknot.setPlainText('')
        self.line_edit.setText('')

    def button_pushed2(self):
        file = open(self.line_edit.text().strip(), 'w')
        print(self.bloknot.toPlainText().strip(), file=file)
        file.close()

    def button_pushed3(self):
        file = open(self.line_edit.text().strip())
        self.bloknot.setPlainText(''.join(file.readlines()))
        self.bloknot.setDisabled(False)
        file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
