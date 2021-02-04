import sys

from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QPushButton, QLabel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QColor, QPainter
from PIL import Image


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle('Рост хорошего настроения')
        self.do_paint = False
        self.sld = QSlider(self)
        self.sld.move(25, 50)
        self.sld.resize(25, 400)
        self.sld.setMaximum(100)
        self.sld.setMinimum(0)
        self.sld.setValue(0)
        self.sld.valueChanged.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            v = self.sld.value()
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 0, 0))
            qp.drawEllipse(100, 62, 3.75 * v, 3.75 * v)
            qp.drawEllipse(100 + 3.75 // 3 * v, 62 + 3.75 // 2 * v, 0.5 * v, 0.5 * v)
            qp.drawEllipse(100 + 3.75 // 3 * v + 1.25 * v, 62 + 3.75 // 2 * v, 0.5 * v, 0.5 * v)
            if v < 25:
                qp.drawArc(100 + 3.75 * v // 2 - v, 62 + 2.5 * v, 2 * v, v, 0, 3000)
            elif 25 <= v <= 50:
                qp.drawLine(100 + 0.75 * v, 62 + 2.82 * v, 100 + 3 * v, 62 + 2.82 * v)
            elif 50 <= v <= 75:
                qp.drawArc(100 + 3.75 * v // 2 - 0.5 * v, 62 + 2 * v, 2 * v, v, -1500, 2000)
            else:
                qp.drawArc(100 + 3.75 * v // 2 - v, 62 + 2 * v, 2 * v, v, -2900, 3000)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
