import sys
from PIL import Image
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QFileDialog


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.font = QFont()
        self.font.setPointSize(14)
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle('PIL 2.0')

        self.btn1 = QPushButton('R', self)
        self.btn1.move(25, 25)
        self.btn1.clicked.connect(self.paint)
        self.btn1.resize(100, 50)
        self.btn1.setFont(self.font)

        self.btn2 = QPushButton('G', self)
        self.btn2.move(25, 100)
        self.btn2.clicked.connect(self.paint)
        self.btn2.resize(100, 50)
        self.btn2.setFont(self.font)

        self.btn3 = QPushButton('B', self)
        self.btn3.move(25, 175)
        self.btn3.clicked.connect(self.paint)
        self.btn3.resize(100, 50)
        self.btn3.setFont(self.font)

        self.btn4 = QPushButton('ALL', self)
        self.btn4.move(25, 250)
        self.btn4.clicked.connect(self.paint)
        self.btn4.resize(100, 50)
        self.btn4.setFont(self.font)

        self.btn5 = QPushButton('Против часовой\nстрелке', self)
        self.btn5.setFont(self.font)
        self.btn5.resize(200, 50)
        self.btn5.move(25, 350)
        self.btn5.clicked.connect(self.spin)

        self.btn6 = QPushButton('По часовой\nстрелке', self)
        self.btn6.setFont(self.font)
        self.btn6.resize(200, 50)
        self.btn6.move(250, 350)
        self.btn6.clicked.connect(self.spin)

        self.image = QLabel(self)
        self.image.move(150, 25)
        self.image.resize(300, 300)
        self.file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.file_name)
        self.image.setPixmap(self.pixmap)

        self.spin_now = 0
        self.color_now = 'ALL'

    def paint(self):
        color = self.sender().text()
        if color == 'ALL':
            self.pixmap = QPixmap(self.file_name)
            self.image.setPixmap(self.pixmap)
        else:
            im = Image.open(self.file_name)
            x, y = im.size
            pixels = im.load()
            self.color_now = color
            for i in range(x):
                for j in range(y):
                    if color == 'R':
                        pixels[i, j] = (pixels[i, j][0], 0, 0)
                    elif color == 'G':
                        pixels[i, j] = (0, pixels[i, j][0], 0)
                    elif color == 'B':
                        pixels[i, j] = (0, 0, pixels[i, j][0])
            for i in range(self.spin_now // 90):
                im = im.transpose(Image.ROTATE_90)
            im.save('temp.png')
            self.pixmap = QPixmap('temp.png')
            self.image.setPixmap(self.pixmap)

    def spin(self):
        im = Image.open(self.file_name)
        x, y = im.size
        pixels = im.load()
        if self.color_now != 'ALL':
            for i in range(x):
                for j in range(y):
                    if self.color_now == 'R':
                        pixels[i, j] = (pixels[i, j][0], 0, 0)
                    elif self.color_now == 'G':
                        pixels[i, j] = (0, pixels[i, j][0], 0)
                    elif self.color_now == 'B':
                        pixels[i, j] = (0, 0, pixels[i, j][0])
        for i in range(self.spin_now // 90):
            im = im.transpose(Image.ROTATE_90)
        vector = self.sender().text()
        if vector == 'По часовой\nстрелке':
            im = im.transpose(Image.ROTATE_90)
            self.spin_now += 90
            self.spin_now %= 360
        else:
            im = im.transpose(Image.ROTATE_270)
            self.spin_now += 270
            self.spin_now %= 360
        im.save('temp.png')
        self.pixmap = QPixmap('temp.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
