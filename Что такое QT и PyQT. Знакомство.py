import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Прятки для виджетов')

        self.box1 = QCheckBox(self)
        self.box1.move(50, 50)
        self.box1.stateChanged.connect(self.box_pushed)
        self.box1.setText('box1')

        self.box2 = QCheckBox(self)
        self.box2.move(50, 100)
        self.box2.stateChanged.connect(self.box_pushed)
        self.box2.setText('box2')

        self.box3 = QCheckBox(self)
        self.box3.move(50, 150)
        self.box3.stateChanged.connect(self.box_pushed)
        self.box3.setText('box3')

        self.box4 = QCheckBox(self)
        self.box4.move(50, 200)
        self.box4.stateChanged.connect(self.box_pushed)
        self.box4.setText('box4')

        self.lbl1 = QLineEdit(self)
        self.lbl1.move(100, 50)
        self.lbl1.setText('Поле box1')
        self.lbl1.setVisible(False)

        self.lbl2 = QLineEdit(self)
        self.lbl2.move(100, 100)
        self.lbl2.setText('Поле box2')
        self.lbl2.setVisible(False)

        self.lbl3 = QLineEdit(self)
        self.lbl3.move(100, 150)
        self.lbl3.setText('Поле box3')
        self.lbl3.setVisible(False)

        self.lbl4 = QLineEdit(self)
        self.lbl4.move(100, 200)
        self.lbl4.setText('Поле box4')
        self.lbl4.setVisible(False)

    def box_pushed(self):
        name = self.sender().text()
        if bool(eval(f'self.{name}.checkState()')):
            eval(f'self.{"lbl" + name[-1]}.setVisible(True)')
        elif not bool(eval(f'self.{name}.checkState()')):
            eval(f'self.{"lbl" + name[-1]}.setVisible(False)')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
