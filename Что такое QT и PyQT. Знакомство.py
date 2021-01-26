import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QCheckBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 390, 100)
        self.setWindowTitle('Азбука Морзе 2')
        self.morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                      'G': '--.',
                      'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
                      'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-',
                      'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..'}

        coef_x = 0
        coef_y = 0
        for name in self.morse.keys():
            btn = QPushButton(self)
            btn.resize(30, 30)
            btn.move(coef_x * 30, coef_y * 30)
            btn.setText(name)
            btn.clicked.connect(self.pushed_button)
            coef_x += 1
            if coef_x == 13:
                coef_x = 0
                coef_y = 1
        self.line = QLineEdit(self)
        self.line.move(0, 60)
        self.line.resize(390, 40)

    def pushed_button(self):
        st = self.sender().text()
        self.line.setText(self.line.text() + self.morse[st])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
