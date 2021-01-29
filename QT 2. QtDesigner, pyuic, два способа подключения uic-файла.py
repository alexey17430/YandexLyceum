import sys
from PyQt5.QtWidgets import QApplication, QRadioButton, QLabel, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
from PyQt5 import QtGui, uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('минипланировщик.ui', self)
        self.setWindowTitle('Минипланировщик')
        self.font1 = QtGui.QFont()
        self.font1.setPointSize(18)
        self.font2 = QtGui.QFont()
        self.font2.setPointSize(12)
        self.font3 = QtGui.QFont()
        self.font3.setPointSize(10)
        self.tasks = dict()

        self.timeEdit.setFont(self.font2)
        self.lineEdit.setFont(self.font2)
        self.pushButton.setFont(self.font2)
        self.pushButton.setText('Добавить событие')
        self.textBrowser.setFont(self.font2)
        self.pushButton.clicked.connect(self.btn_pushed)

    def btn_pushed(self):
        date_for_task = str(self.calendarWidget.selectedDate())
        date_for_task = date_for_task[date_for_task.index('(') + 1: date_for_task.index(')')]
        date_for_task = list(int(i) for i in date_for_task.split(', '))
        time_for_task = list(int(i) for i in str(self.timeEdit.text()).split(':'))
        key = tuple(date_for_task + time_for_task)
        self.tasks[key] = self.lineEdit.text()
        self.textBrowser.setPlainText('')
        for key in sorted(self.tasks.keys()):
            new_key = list(map(str, list(key)))
            self.textBrowser.setPlainText(self.textBrowser.toPlainText()
                                          + '\n' + f"{new_key[0]}-{new_key[1]}-{new_key[2]} "
                                                   f"{new_key[3]}:{new_key[4]} "
                                                   f"{self.tasks[key]}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
