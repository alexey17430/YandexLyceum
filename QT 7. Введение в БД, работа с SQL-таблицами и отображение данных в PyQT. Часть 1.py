import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox, QPlainTextEdit, QComboBox
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 350, 600, 400)
        self.setWindowTitle('Поиск по фильмам')
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()
        self.font = QFont()
        self.font.setPointSize(12)

        self.btn = QPushButton(self)
        self.btn.move(475, 20)
        self.btn.resize(100, 30)
        self.btn.setText('Поиск')
        self.btn.setFont(self.font)
        self.btn.clicked.connect(self.btn_pushed)

        self.box = QComboBox(self)
        self.box.move(25, 20)
        self.box.resize(175, 30)
        self.box.setFont(self.font)
        self.box.addItem('Год выпуска')
        self.box.addItem('Название')
        self.box.addItem('Продолжительность')

        self.edit = QLineEdit(self)
        self.edit.move(225, 20)
        self.edit.resize(225, 30)
        self.edit.setFont(self.font)

        self.lbl1 = QLabel(self)
        self.lbl1.move(25, 70)
        self.lbl1.resize(175, 30)
        self.lbl1.setText('ID:')
        self.lbl1.setFont(self.font)

        self.lbl2 = QLabel(self)
        self.lbl2.move(25, 120)
        self.lbl2.resize(175, 30)
        self.lbl2.setText('Название:')
        self.lbl2.setFont(self.font)

        self.lbl3 = QLabel(self)
        self.lbl3.move(25, 170)
        self.lbl3.resize(175, 30)
        self.lbl3.setText('Год выпуска:')
        self.lbl3.setFont(self.font)

        self.lbl4 = QLabel(self)
        self.lbl4.move(25, 220)
        self.lbl4.resize(175, 30)
        self.lbl4.setText('Жанр:')
        self.lbl4.setFont(self.font)

        self.lbl5 = QLabel(self)
        self.lbl5.move(25, 270)
        self.lbl5.resize(175, 30)
        self.lbl5.setText('Продолжительность:')
        self.lbl5.setFont(self.font)

        self.lbl6 = QLabel(self)
        self.lbl6.move(25, 320)
        self.lbl6.resize(550, 30)
        self.lbl6.setText('')
        self.lbl6.setFont(self.font)

        self.edit1 = QLineEdit(self)
        self.edit1.move(225, 70)
        self.edit1.resize(350, 30)
        self.edit1.setFont(self.font)

        self.edit2 = QLineEdit(self)
        self.edit2.move(225, 120)
        self.edit2.resize(350, 30)
        self.edit2.setFont(self.font)

        self.edit3 = QLineEdit(self)
        self.edit3.move(225, 170)
        self.edit3.resize(350, 30)
        self.edit3.setFont(self.font)

        self.edit4 = QLineEdit(self)
        self.edit4.move(225, 220)
        self.edit4.resize(350, 30)
        self.edit4.setFont(self.font)

        self.edit5 = QLineEdit(self)
        self.edit5.move(225, 270)
        self.edit5.resize(350, 30)
        self.edit5.setFont(self.font)

    def btn_pushed(self):
        name_table = self.box.currentText()
        znach = self.edit.text()

        if name_table == 'Год выпуска':
            name_table = 'year'
        elif name_table == 'Название':
            name_table = 'title'
        elif name_table == 'Продолжительность':
            name_table = 'duration'

        if name_table == 'title':
            res = self.cur.execute(f'''select * from films 
                        where {name_table} like "{znach}"''').fetchone()
        else:
            res = self.cur.execute(f'''select * from films 
            where {name_table} == {znach}''').fetchone()

        if res is None:
            self.lbl6.setText('Ничего не найдено')
        else:
            res = list(map(str, res))
            self.edit1.setText(res[0])
            self.edit2.setText(res[1])
            self.edit3.setText(res[2])
            id = int(res[3])
            gen = self.cur.execute(f'''
            select title from genres where id = {id}''').fetchone()
            self.edit4.setText(gen[0])
            self.edit5.setText(res[4])
            self.lbl6.setText('Поиск успешно выполнен')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
