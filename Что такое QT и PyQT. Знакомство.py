import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QCheckBox, QRadioButton, QMainWindow
from PyQt5 import QtGui, uic


class QPushButton1(QPushButton):
    def __init__(self, obj, name, poz):
        super().__init__(obj)
        self.name = name
        self.poz = poz


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('крестики нолики.ui', self)

        self.btn_new_game = QPushButton(self)
        self.btn_new_game.resize(150, 40)
        self.btn_new_game.setText('Новая игра')
        self.btn_new_game.move(125, 500)
        self.btn_new_game.clicked.connect(self.btn_new_game_push)
        self.font = QtGui.QFont()
        self.font.setPointSize(30)
        self.font1 = QtGui.QFont()
        self.font1.setPointSize(14)
        self.radioButton_1.setFont(self.font)
        self.radioButton_2.setFont(self.font)
        self.radioButton_1.setChecked(True)
        self.btn_new_game.setFont(self.font1)
        self.new_game()

        #self.radio_btn_x = QRadioButton('X')
        #self.radio_btn_x.setChecked(True)
        #self.radio_btn_x.toggled.connect(self.onClicked)
        #self.radio_btn_x.move(100, 50)
        #self.radio_btn_x.resize(50, 50)

        #self.radio_btn_o = QRadioButton('O')
        #self.radio_btn_o.setChecked(False)
        #self.radio_btn_o.toggled.connect(self.onClicked)
        #self.radio_btn_o.move(200, 50)
        #self.radio_btn_o.resize(50, 50)

        #self.layout.addWidget(self.radio_btn_x, 0, 0)
        #self.layout.addWidget(self.radio_btn_o, 0, 1)

    def btn_new_game_push(self):
        self.win_lbl.setText('')
        if self.radioButton_1.isChecked():
            self.hod_now = 1
        else:
            self.hod_now = -1
        for i in range(3):
            for j in range(3):
                self.squers[i][j].setText('')
                self.squers[i][j].setDisabled(False)

    def squer_pushed(self):
        def win_proverka(self, znak):
            # проверка горизонтали
            for line in self.squers:
                if line[0].text() == znak and line[1].text() == znak and \
                        line[2].text() == znak:
                    return True
            # проверка по вертикали
            if self.squers[0][0].text() == znak and \
                    self.squers[1][0].text() == znak and \
                    self.squers[2][0].text() == znak or \
                    self.squers[0][1].text() == znak and \
                    self.squers[1][1].text() == znak and \
                    self.squers[2][1].text() == znak or \
                    self.squers[0][2].text() == znak and \
                    self.squers[1][2].text() == znak and \
                    self.squers[2][2].text() == znak:
                return True
            if self.squers[0][0].text() == znak and \
                    self.squers[1][1].text() == znak and \
                    self.squers[2][2].text() == znak or \
                    self.squers[0][2].text() == znak and \
                    self.squers[1][1].text() == znak and \
                    self.squers[2][0].text() == znak:
                return True
            return False

        i, j = self.sender().poz
        i = int(i)
        j = int(j)
        if self.hod_now == 1:
            self.squers[i][j].setText('X')
        else:
            self.squers[i][j].setText('O')
        self.hod_now *= -1
        self.squers[i][j].setDisabled(True)
        if win_proverka(self, 'X'):
            self.win_lbl.setText('Крестики победили')
            for i in range(3):
                for j in range(3):
                    self.squers[i][j].setDisabled(True)
        elif win_proverka(self, 'O'):
            self.win_lbl.setText('Нолики победили')
            for i in range(3):
                for j in range(3):
                    self.squers[i][j].setDisabled(True)
        else:
            draw_flag = True
            for i in range(3):
                for j in range(3):
                    if self.squers[i][j].text() != 'X' and self.squers[i][j].text() != 'O':
                        draw_flag = False
                        break
            if draw_flag:
                self.win_lbl.setText('Ничья')

    def new_game(self):
        self.setGeometry(550, 150, 400, 600)
        self.setWindowTitle('Крестики-нолики')
        self.win_lbl = QLabel(self)
        self.win_lbl.setFont(self.font1)
        self.win_lbl.move(125, 550)
        self.win_lbl.resize(200, 50)
        if self.radioButton_1.isChecked():
            self.hod_now = 1
        else:
            self.hod_now = -1
        self.squers = list()
        n = 1
        for i in range(3):
            line = list()
            for j in range(3):
                btn = QPushButton1(self, f'btn{n}', (i, j))
                btn.move(55 + 100 * j, 155 + 100 * i)
                btn.resize(90, 90)
                btn.setText('')
                btn.setFont(self.font)
                btn.clicked.connect(self.squer_pushed)
                line.append(btn)
                n += 1
            self.squers.append(line)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
