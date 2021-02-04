import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('square.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        self.font = QFont()
        self.font.setPointSize(14)

        self.pushButton.setFont(self.font)
        self.label.setFont(self.font)
        self.label_2.setFont(self.font)
        self.label_3.setFont(self.font)
        self.spinBox.setFont(self.font)
        self.doubleSpinBox.setFont(self.font)
        self.spinBox_2.setFont(self.font)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor('red'))
            delta = 0
            start = self.side
            for i in range(self.n):
                qp.drawRect(50 + delta, 125 + delta, self.side, self.side)
                delta = (start - round(self.k * self.side)) // 2
                self.side = round(self.k * self.side)
            qp.end()

    def paint(self):
        self.side = self.spinBox.value()
        self.k = self.doubleSpinBox.value()
        self.n = self.spinBox_2.value()
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
