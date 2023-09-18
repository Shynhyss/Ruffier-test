'''тут написан второй экран'''
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import(QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit)

from instr import* # Берём параметры текста из текстовой части кода
from final_win import* # Берём параметры последнего(третьего) окна


class Experiment():
    def __init__(self, age, test1, test2, test3):
        '''окно, в котором проводится опрос'''
        super().__init__()
