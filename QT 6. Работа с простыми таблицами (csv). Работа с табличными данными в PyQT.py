# имя файла - information.csv
import sys
import csv
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5 import QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 575)
        self.setWindowTitle('Интерактивный чек')
        font = QtGui.QFont()
        font.setPointSize(16)
        screen_font = QtGui.QFont()
        screen_font.setPointSize(20)

        self.btn = QPushButton(self)
        self.btn.move(50, 425)
        self.btn.setText('Итого')
        self.btn.resize(150, 50)
        self.btn.setFont(screen_font)
        self.btn.clicked.connect(self.button_pushed)

        self.edit = QLineEdit(self)
        self.edit.move(250, 425)
        self.edit.resize(200, 50)
        self.edit.setFont(screen_font)

        self.btn_repaint = QPushButton(self)
        self.btn_repaint.move(150, 500)
        self.btn_repaint.resize(200, 50)
        self.btn_repaint.setFont(screen_font)
        self.btn_repaint.setText('Обновить')
        self.btn_repaint.clicked.connect(self.button_repaint_pushed)

        file = open('information.csv', encoding='UTF-8')
        reader = list(csv.reader(file, delimiter=';'))
        self.table = QTableWidget(self)
        self.table.setFont(font)
        self.table.move(50, 50)
        self.table.resize(400, 350)
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 240)
        self.table.setColumnWidth(1, 50)
        self.table.setColumnWidth(2, 75)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Название'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Цена'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Кол-во'))
        self.table.setRowCount(len(list(reader)))
        self.table.setAlternatingRowColors(True)
        self.reader = list(reader)

        n = 0
        for elem in sorted(self.reader, key=lambda x: int(x[1]))[::-1]:
            name, cost = elem
            self.table.setItem(n, 0, QTableWidgetItem(name))
            self.table.setItem(n, 1, QTableWidgetItem(cost))
            self.table.setItem(n, 2, QTableWidgetItem('0'))
            n += 1

    def button_pushed(self):
        su = 0
        for i in range(len(self.reader)):
            su += int(self.table.item(i, 1).text()) * int(self.table.item(i, 2).text())
        self.edit.setText(str(su))

    def button_repaint_pushed(self):
        for i in range(len(self.reader)):
            if i == 5:
                break
            color = (randint(1, 255), randint(1, 255), randint(1, 255))
            self.table.item(i, 0).setBackground(QtGui.QColor(*color))
            self.table.item(i, 1).setBackground(QtGui.QColor(*color))
            self.table.item(i, 2).setBackground(QtGui.QColor(*color))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
