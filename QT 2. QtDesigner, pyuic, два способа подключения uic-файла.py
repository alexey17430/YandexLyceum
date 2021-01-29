import sys
from PyQt5.QtWidgets import QApplication, QRadioButton, QLabel, QPlainTextEdit, QDoubleSpinBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle('Антиплагиат')

        self.font1 = QtGui.QFont()
        self.font1.setPointSize(18)
        self.font2 = QtGui.QFont()
        self.font2.setPointSize(12)
        self.font3 = QtGui.QFont()
        self.font3.setPointSize(10)

        self.lbl = QLabel(self)
        self.lbl.move(25, 25)
        self.lbl.setFont(self.font1)
        self.lbl.setText('Порог срабатывания(%):')
        self.lbl.resize(280, 50)

        self.box = QDoubleSpinBox(self)
        self.box.move(325, 25)
        self.box.resize(150, 50)
        self.box.setFont(self.font1)
        self.box.setValue(85)

        self.btn = QPushButton(self)
        self.btn.move(500, 25)
        self.btn.resize(275, 50)
        self.btn.setText('Сравнить')
        self.btn.setFont(self.font1)
        self.btn.clicked.connect(self.btn_pushed)
        self.btn

        self.edit1 = QPlainTextEdit(self)
        self.edit1.move(25, 175)
        self.edit1.resize(350, 400)
        self.edit1.setFont(self.font2)

        self.edit2 = QPlainTextEdit(self)
        self.edit2.move(425, 175)
        self.edit2.resize(350, 400)
        self.edit2.setFont(self.font2)

        self.lbl1 = QLabel(self)
        self.lbl1.setText('Текст №1')
        self.lbl1.move(25, 145)
        self.lbl1.resize(250, 25)
        self.lbl1.setFont(self.font1)

        self.lbl2 = QLabel(self)
        self.lbl2.setText('Текст №2')
        self.lbl2.move(425, 145)
        self.lbl2.resize(250, 25)
        self.lbl2.setFont(self.font1)

        self.res_lbl = QLabel(self)
        self.res_lbl.move(250, 85)
        self.res_lbl.resize(300, 50)
        self.res_lbl.setFont(self.font1)
        self.res_lbl.setText('')

    def btn_pushed(self):
        st1 = self.edit1.toPlainText().split('\n')
        st2 = self.edit2.toPlainText().split('\n')
        lines = 0
        for i in range(min(len(st1), len(st2))):
            l1 = st1[i]
            l2 = st2[i]
            if l1 == l2:
                lines += 1
        self.res_lbl.setText(f'Код похож на {round(lines / max(len(st1), len(st2)), 4) * 100}%')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
