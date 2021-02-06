# имя файла - information.csv
import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5 import QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Интерактивный чек')
        font = QtGui.QFont()
        font.setPointSize(16)
        screen_font = QtGui.QFont()
        screen_font.setPointSize(30)

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
        self.reader = list(reader)

        n = 0
        for elem in reader:
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
