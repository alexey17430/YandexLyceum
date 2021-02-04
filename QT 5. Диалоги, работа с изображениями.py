import sys

from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QPushButton, QLabel
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle('Управление прозрачностью')
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]

        self.sld = QSlider(self)
        self.sld.move(25, 100)
        self.sld.resize(25, 300)
        self.sld.setMaximum(250)
        self.sld.setMinimum(0)
        self.sld.setValue(250)
        self.sld.valueChanged.connect(self.change_slider)

        self.pixmap = QPixmap(self.fname)
        self.image = QLabel(self)
        self.image.move(75, 25)
        self.image.resize(400, 450)
        self.image.setPixmap(self.pixmap)

    def change_slider(self):
        im = Image.open(self.fname)
        v = self.sld.value()
        im.putalpha(v)
        im.save('temp.png')
        self.image.setPixmap(QPixmap('temp.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
