import sys
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 500, 500)
        self.setWindowTitle('Супрематизм')
        self.button = ''
        self.coords = tuple()
        self.coords_space = tuple()
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.coords = (event.x(), event.y())
        if event.button() == Qt.LeftButton:
            self.button = 'left'
            self.update()
        else:
            self.button = 'right'
            self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.button = 'space'
            self.update()

    def mouseMoveEvent(self, event):
        self.coords_space = (event.x(), event.y())

    def paintEvent(self, event):
        if self.button == 'left':
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            r = randint(50, 350)
            qp.drawEllipse(self.coords[0] - (r // 4), self.coords[1] - (r // 4), r // 2, r // 2)
            qp.end()
        elif self.button == 'right':
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            a = randint(15, 200)
            b = randint(15, 200)
            qp.drawRect(self.coords[0] - a // 2, self.coords[1] - b // 2, a, b)
            qp.end()
        elif self.button == 'space':
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            a = randint(15, 200)
            x, y = self.coords_space
            qp.drawPolygon(QPoint(x - a // 2, y + a // 2),
                           QPoint(x + a // 2, y + a // 2),
                           QPoint(x, y - a // 2))
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
