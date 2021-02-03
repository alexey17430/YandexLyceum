import sys
from PyQt5.QtWidgets import QApplication, QRadioButton, QLabel
from PyQt5.QtWidgets import QMainWindow, QButtonGroup, QLineEdit
from PyQt5 import QtGui, uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('файловая статистика.ui', self)
        self.setWindowTitle('файловая статистика')
        self.font1 = QtGui.QFont()
        self.font1.setPointSize(18)
        self.font2 = QtGui.QFont()
        self.font2.setPointSize(12)
        self.font3 = QtGui.QFont()
        self.font3.setPointSize(10)
        self.lineEdit_1.setFont(self.font2)
        self.lineEdit_2.setFont(self.font2)
        self.lineEdit_3.setFont(self.font2)
        self.lineEdit_4.setFont(self.font2)

        for i in range(1, 5):
            eval(f'self.label_{i}.setFont(self.font2)')
        self.pushButton.clicked.connect(self.btn_pushed)

    def btn_pushed(self):
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        file_name = self.lineEdit_1.text()
        try:
            if '.txt' not in file_name:
                raise IndexError
            file = open(file_name.strip())
            all_lines = list(map(lambda x: (x.strip()), file.readlines()))
            numbers = list()
            for line in all_lines:
                flag = True
                for i in line:
                    if i not in '1234567890':
                        flag = False
                if flag:
                    numbers.append(float(line))
            ma = max(numbers)
            mi = min(numbers)
            sr = round(sum(numbers) / len(numbers), 2)
            file.close()
            ans_file = open('output.txt', 'w')
            ans_file.write(f'{ma}\n{mi}\n{sr}\n\n')
            self.lineEdit_2.setText(str(ma))
            self.lineEdit_3.setText(str(mi))
            self.lineEdit_4.setText(str(sr))
            self.label.setFont(self.font2)
            self.label.setText('Все преобразования выполнены успешно')
        except IndexError:
            self.label.setFont(self.font2)
            self.label.setText('Файл содержит некоректное расширение')
        except TypeError:
            self.label.setFont(self.font2)
            self.label.setText('В файле содержатся некоректные данные')
        except FileNotFoundError:
            self.label.setFont(self.font2)
            self.label.setText('Необходимый файл не найден')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
