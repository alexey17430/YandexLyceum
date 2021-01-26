import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Вычисление выражений')
        self.btn = QPushButton('->', self)
        self.btn.move(180, 180)
        self.btn.resize(40, 40)
        self.btn.clicked.connect(self.btn_pushed)

        self.name_input_first = QLineEdit(self)
        self.name_input_first.move(40, 180)
        self.name_input_first.resize(120, 40)

        self.lbl_first = QLabel(self)
        self.lbl_first.setText('Выражение:')
        self.lbl_first.move(40, 160)
        self.lbl_first.adjustSize()

        self.name_input_second = QLineEdit(self)
        self.name_input_second.move(240, 180)
        self.name_input_second.resize(120, 40)

        self.lbl_second = QLabel(self)
        self.lbl_second.setText('Результат:')
        self.lbl_second.move(240, 160)

    def btn_pushed(self):
        if self.btn.text() == '->':
            self.name_input_second.setText(str(eval(self.name_input_first.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
