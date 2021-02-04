import sys
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPixmap, QFont, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QFileDialog, QInputDialog
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.font = QFont()
        self.font.setPointSize(14)
        self.setGeometry(500, 200, 300, 300)
        self.setWindowTitle('Генерация флага')

        self.btn = QPushButton(self)
        self.btn.setText('Ввести количество\nцветов флага')
        self.btn.resize(200, 50)
        self.btn.move(50, 25)
        self.btn.setFont(self.font)
        self.btn.clicked.connect(self.button_pushed)

        self.image = QLabel(self)
        self.image.move(50, 100)
        self.image.resize(200, 120)

    def button_pushed(self):
        colvo, ok_pressed = QInputDialog.getInt(self, "Введите количество цветов",
                                                "Сколько цветов?",
                                                3, 1, 5, 1)
        im = Image.new('RGB', (200, 120), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        if ok_pressed:
            for i in range(int(colvo)):
                draw.rectangle((0, 120 // colvo * i, 200, 120 // colvo * (i + 1)),
                               fill=(randint(1, 255), randint(1, 255), randint(1, 255)), width=5)
        im.save('picture.png')
        self.pixmap = QPixmap('picture.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
