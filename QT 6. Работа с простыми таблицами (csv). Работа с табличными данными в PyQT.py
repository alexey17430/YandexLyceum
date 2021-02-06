import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit, QComboBox, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QFont, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 600, 600)
        self.setWindowTitle('Результат олимпиады: фильтрация')
        self.font = QFont()
        self.font.setPointSize(12)
        file = open('rez.csv', encoding='UTF-8')
        self.reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
        self.schools = set()
        self.classes = set()
        for elem in self.reader:
            self.schools.add(elem['login'].split('-')[2])
            self.classes.add(elem['login'].split('-')[-2])
        self.box1 = QComboBox(self)
        self.box1.move(30, 25)
        self.box1.resize(160, 25)
        self.box1.setFont(self.font)
        self.box1.addItem('Все')
        for elem in self.schools:
            self.box1.addItem(elem)

        self.box2 = QComboBox(self)
        self.box2.move(220, 25)
        self.box2.resize(160, 25)
        self.box2.setFont(self.font)
        self.box2.addItem('Все')
        for elem in self.classes:
            self.box2.addItem(elem)

        self.btn = QPushButton(self)
        self.btn.move(410, 25)
        self.btn.resize(160, 25)
        self.btn.setFont(self.font)
        self.btn.setText('Узнать результаты')
        self.btn.clicked.connect(self.btn_pushed)

        self.table = QTableWidget(self)
        self.table.move(25, 75)
        self.table.resize(550, 500)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Фамилия'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Результат'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('Логин'))

    def btn_pushed(self):
        school = self.box1.currentText()
        cls = self.box2.currentText()
        ans = list()
        for elem in self.reader:
            if (school == 'Все' or school == elem['login'].split('-')[2]) and \
                    (cls == 'Все' or cls == elem['login'].split('-')[-2]):
                ans.append((elem['user_name'].split()[3], elem['Score'], elem['user_name']))
        self.table.setRowCount(len(ans))
        winners = set()
        for i in range(len(ans)):
            elem = ans[i]
            winners.add(elem[1])
            self.table.setItem(i, 0, QTableWidgetItem(elem[0]))
            self.table.setItem(i, 1, QTableWidgetItem(elem[1]))
            self.table.setItem(i, 2, QTableWidgetItem(elem[2]))
            if len(winners) == 1:
                self.table.item(i, 0).setBackground(QColor('gold'))
            elif len(winners) == 2:
                self.table.item(i, 0).setBackground(QColor(197, 201, 199))
            elif len(winners) == 3:
                self.table.item(i, 0).setBackground(QColor(205, 127, 50))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
