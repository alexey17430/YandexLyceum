import sys
from PyQt5.QtWidgets import QApplication, QRadioButton, QLabel, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
from PyQt5 import QtGui, uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('записная книжка.ui', self)
        self.setWindowTitle('Записная книжка')
        self.font1 = QtGui.QFont()
        self.font1.setPointSize(18)
        self.font2 = QtGui.QFont()
        self.font2.setPointSize(12)
        self.font3 = QtGui.QFont()
        self.font3.setPointSize(10)

        self.edit = QPlainTextEdit(self)
        self.edit.move(40, 150)
        self.edit.resize(400, 230)
        self.edit.setFont(self.font1)

        self.label_1.setFont(self.font2)
        self.label_2.setFont(self.font2)
        self.pushButton.setFont(self.font2)
        self.pushButton.clicked.connect(self.btn_pushed)
        self.lineEdit_1.setFont(self.font2)
        self.lineEdit_2.setFont(self.font2)

    def btn_pushed(self):
        name = self.lineEdit_1.text()
        number = self.lineEdit_2.text()
        self.edit.setPlainText(self.edit.toPlainText() + name + ' ' + number + '\n')
        self.lineEdit_1.setText('')
        self.lineEdit_2.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
