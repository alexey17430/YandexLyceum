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
        self.setWindowTitle('Управление НЛО')
        self.x, self.y = 10, 10
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        qp.setBrush(QColor(150, 150, 150))
        qp.setPen(QColor(150, 150, 150))
        qp.drawEllipse(self.x, self.y, 70, 40)
        qp.setBrush(QColor(0, 0, 0))
        qp.setPen(QColor(0, 0, 0))
        qp.drawEllipse(self.x + 25, self.y + 10, 20, 20)
        qp.end()

    def keyPressEvent(self, event):
        if int(event.key()) == 16777234:  # влево
            self.x -= 10
            if self.x < 0:
                self.x = 430
            self.update()
        elif int(event.key()) == 16777236:  # вправо
            self.x += 10
            if self.x > 430:
                self.x = 0
            self.update()
        elif int(event.key()) == 16777235:  # вверх
            self.y -= 10
            if self.y < 0:
                self.y = 460
            self.update()
        elif int(event.key()) == 16777237:  # вниз
            self.y += 10
            if self.y > 460:
                self.y = 0
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
