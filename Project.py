# Импортируем потоковый ввод
import sys
# Импортируем интерфейс
from design import Ui_MainWindow
# Импортируем функцию для вычисления радикала
from math import sqrt
# Импортируем функции для работы программы
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


num1 = 0.0
num2 = 0.0
sumit = 0.0
sumall = 0.0
operator = ""
m = 0.0
flag = False


# Основной класс
class Calc(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Назначаем строку только для чтения
        self.lineEdit.setReadOnly(True)

        # Равнение ввода по правому краю
        self.lineEdit.setAlignment(Qt.AlignRight)

        # Блок кликов:
        self.zero.clicked.connect(self.Num)
        self.one.clicked.connect(self.Num)
        self.two.clicked.connect(self.Num)
        self.three.clicked.connect(self.Num)
        self.four.clicked.connect(self.Num)
        self.five.clicked.connect(self.Num)
        self.six.clicked.connect(self.Num)
        self.seven.clicked.connect(self.Num)
        self.eight.clicked.connect(self.Num)
        self.nine.clicked.connect(self.Num)
        self.plus.clicked.connect(self.operator)
        self.minus.clicked.connect(self.operator)
        self.multiply.clicked.connect(self.operator)
        self.divide.clicked.connect(self.operator)
        self.equality.clicked.connect(self.operator)
        self.comma.clicked.connect(self.Comma)
        self.switch_sign.clicked.connect(self.Switch)
        self.radical.clicked.connect(self.Radical)
        self.percent.clicked.connect(self.Percent)
        self.one_divide_by_x.clicked.connect(self.O_D_B_X)
        self.c.clicked.connect(self.C)
        self.ce.clicked.connect(self.CE)
        self.bdel.clicked.connect(self.DEL)
        self.mc.clicked.connect(self.MC)
        self.mr.clicked.connect(self.MR)
        self.ms.clicked.connect(self.MS)
        self.mplus.clicked.connect(self.Mplus)
        self.mminus.clicked.connect(self.Mminus)

    # Блок функций для кнопок:

    # Функция чисел
    def Num(self):
        global num1
        global num2
        global flag

        sender = self.sender()

        num2 = int(sender.text())
        setnum = str(num2)

        if flag:
            self.lineEdit.setText(setnum)
            flag = False
        
        else:
            self.lineEdit.setText(self.lineEdit.text() + setnum)

    # Функция оператора        
    def operator(self):
        global sumit
        global num1
        global flag
        global operator

        sumit += 1

        if sumit > 1:
            self.Equality()

        num1 = self.lineEdit.text()
        sender = self.sender()
        operator = sender.text()

        flag = True

    # Функция вывода конечного результата
    def Equality(self):
        global sumit
        global sumall
        global num1
        global num2
        global operator
        global control

        sumit = 0

        num2 = self.lineEdit.text()

        # Сложение
        if operator == "+":
            sumall = float(num1) + float(num2)
       
        # Вычитание
        elif operator == "-":
            sumall = float(num1) - float(num2)
       
        # Умножение
        elif operator == "*":
            sumall = float(num1) * float(num2)
        
        # Деление
        elif operator == "/":
            
            if num2 != "0":
                sumall = float(num1) / float(num2)
            
            else:
                sumall = "Ошибка!"
            
        self.lineEdit.setText(str(sumall))
        flag = True
        
    # Функция извлечения корня
    def Radical(self):
        global num1

        if self.lineEdit.text() != '':
        
            num1 = float(self.lineEdit.text())
            num1 = sqrt(num1)
        
            self.lineEdit.setText(str(num1))
        
    # Функция плавающей точки
    def Comma(self):
        if "." not in self.lineEdit.text():
            self.lineEdit.setText(self.lineEdit.text() + ".")

    # Функция изменения знака перед числом
    def Switch(self):
        global num1

        if self.lineEdit.text() != '':
            
            num1 = float(self.lineEdit.text())
            num1 = -num1
        
            self.lineEdit.setText(str(num1))
        
    # Функция процента
    def Percent(self):
        global num1
        global num2

        if num1 != 0.0 and self.lineEdit.text() != '':
            num2 = (float(num2) / 100) * float(num1)
            self.lineEdit.setText(str(num2))

    # Функция деления 1 на х
    def O_D_B_X(self):
        global sumit
        global sumall
        global num1
        global num2
        global flag

        if self.lineEdit.text() != '':
            
            sumit = 0

            num1 = 1.0
            num2 = self.lineEdit.text()

            if num2 != "0":
                sumall = float(num1) / float(num2)
            
            else:
                sumall = "Ошибка!"
            
            self.lineEdit.setText(str(sumall))
            flag = True

    # Функция удаления одного символа
    def DEL(self):
        self.lineEdit.backspace()
        
    # Функция сброс текущей строки
    def CE(self):
        self.lineEdit.clear()

    # Функция сброса всех символов и строки
    def C(self):
        global num1
        global num2
        global sumall
        global operator

        self.lineEdit.clear()

        num1 = 0.0
        num2 = 0.0
        sumall = 0.0
        operator = ""

    # Функция добавления числа в память
    def MS(self):
        global m

        if self.lineEdit.text().isdigit():
            m = float(self.lineEdit.text())

    # Функция показа числа в памяти
    def MR(self):
        global m

        self.lineEdit.clear()
        self.lineEdit.setText(str(m))

    # Функция удаления числа из памяти
    def MC(self):
        global m

        m = 0.0

    # Функция добавления в память суммы памяти и числа
    def Mplus(self):
        global m

        if self.lineEdit.text().isdigit():
            m += float(self.lineEdit.text())

    # Функция добавления в память разности памяти и числа
    def Mminus(self):
        global m

        if self.lineEdit.text().isdigit():
            m -= float(self.lineEdit.text())

# Завершающий этап
if __name__ == "__main__":
    app = QApplication(sys.argv)
    res = Calc()
    res.show()
    sys.exit(app.exec())
