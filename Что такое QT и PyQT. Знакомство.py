import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Фокус со словами')
        self.btn = QPushButton('->', self)
        self.btn.move(180, 180)
        self.btn.resize(40, 40)
        self.btn.clicked.connect(self.btn_pushed)

        self.name_input_first = QLineEdit(self)
        self.name_input_first.move(40, 180)
        self.name_input_first.resize(120, 40)

        self.name_input_second = QLineEdit(self)
        self.name_input_second.move(240, 180)
        self.name_input_second.resize(120, 40)

    def btn_pushed(self):
        if self.btn.text() == '->':
            line_edit_name = self.name_input_first.text()
            self.name_input_second.setText(line_edit_name)
            self.name_input_first.setText('')
            self.btn.setText('<-')
        else:
            line_edit_name = self.name_input_second.text()
            self.name_input_first.setText(line_edit_name)
            self.name_input_second.setText('')
            self.btn.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
