'''тут написан первый экран'''
from PyQt5.QtCore import Qt, QTime, QTimer 
from PyQt5.QtGui import QFont # проверка вводимых значений
from PyQt5.QtWidgets import(QApplication, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, )

from instr import* # Берём параметры текста из текстовой части кода
from second_win import* # Берём параметры второго окна

class MainWin(QWidget):
    def __init__(self):
        '''окно в котором распологается приветствие'''
        super().__init__() # создаём супер класс
        self.initUI()  # создаём и настраиваем графические элементы:
        self.connects() # устанавливаем связи между элементами
        self.set_appear() # устанавливает как будет выглядеть окно (надпись, размер, место)
        self.show() # старт

    def initUI(self):
        '''создаёт графические элементы'''
        self.btn_next = QPushButton(txt_next) # подключаем ранее записаанные тексты
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.Layout = QVBoxLayout()
        self.Layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.Layout.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.Layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self): # переход на второе окно
        self.tx = TestWin()
        self.hide()

    def connects(self): # переход на второе окно
        self.btn_next.clicked.connect(self.next_click) 
        
    '''устанавливает как будет выглядеть окно (надпись, размер, место)'''
    def set_appear(self):
        self.setWindowTitle(txt_title) # название окна
        set.resize(win_width, win_height) # размер окна
        self.move(win_x, win_y) # начальное расположение окна

app = QApplication([])
mw = MainWin()
app.exec()
