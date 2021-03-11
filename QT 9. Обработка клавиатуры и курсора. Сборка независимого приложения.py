import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QPoint
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 500, 500)
        self.setWindowTitle('Убегающая кнопка')
        self.x, self.y = 175, 230
        self.setMouseTracking(True)
        font = QFont()
        font.setPointSize(16)

        self.btn = QPushButton(self)
        self.btn.setText('Нажми меня')
        self.btn.resize(150, 40)
        self.btn.move(175, 230)
        self.btn.setFont(font)

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        if self.x - 15 < x < self.x + 115 or self.y - 15 < y < self.y + 55:
            self.x, self.y = randint(0, 350), randint(0, 460)
            self.btn.move(self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
