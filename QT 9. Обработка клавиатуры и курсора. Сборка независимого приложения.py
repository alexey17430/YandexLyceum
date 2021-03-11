import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 500, 500)
        self.setWindowTitle('Машинка')
        self.x, self.y = 0, 0
        self.setMouseTracking(True)
        self.color1 = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.color2 = QColor(randint(0, 255), randint(0, 255), randint(0, 255))

    def mouseMoveEvent(self, event):
        self.x, self.y = event.x(), event.y()
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(self.color1)
        qp.drawRect(self.x - 50, self.y - 50, 100, 100)
        qp.drawEllipse(self.x - 25, self.y - 100, 50, 50)
        qp.setBrush(self.color2)
        qp.drawEllipse(self.x - 80, self.y - 25, 30, 30)
        qp.drawEllipse(self.x + 50, self.y - 25, 30, 30)
        qp.drawEllipse(self.x - 50, self.y + 50, 30, 30)
        qp.drawEllipse(self.x + 20, self.y + 50, 30, 30)
        qp.setBrush(QColor(255, 91, 0))
        qp.drawEllipse(self.x - 7, self.y - 70, 15, 15)
        qp.drawEllipse(self.x - 15, self.y - 90, 10, 10)
        qp.drawEllipse(self.x + 15, self.y - 90, 10, 10)
        qp.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.color1 = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            self.color2 = QColor(randint(0, 255), randint(0, 255), randint(0, 255))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
