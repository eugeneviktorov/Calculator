import tkinter as tk    #Библиотека графического интерфейса
from tkinter import *    #Библеотека граф.интерфейса(импорт)
from tkinter import messagebox    #Библиотека вывода отдельного окна



block =tk.Tk()    #Обращение к модулю ткинтер
block.geometry(f'360x575+10+10')    #Размеры окна(+10+10 это открытие окна относительно левого верхнего края)
block.maxsize(width=360, height=575)    #Ограничения на изменения окна.
block['bg'] = '#e3e3e3'    #Цвет заднего фона
block.title('Калькулятор')    #Заглавный текст

bend = tk.Entry(block, justify=tk.RIGHT, font=('Ariel',15))    #Поле ввода    #justify(Обращение к консоли вывода и привязка к правой стороне)
bend.insert(0,'0')    #Поле ввода начинается с значения ноль
bend['state'] = tk.DISABLED    #Блокировка ввода текста в поле ввода
bend.grid(row=0, column=0, columnspan=4, stick='we', padx=5, pady=5)    #row(высота объекта) #columnspan(Объединение нескольких колонн)



def key_pressed(event):    #Бинд кнопок на клавиатуре
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char in '.':
        add_operation(event.char)
    elif event.char in '(':
        add_operation(event.char)
    elif event.char in ')':
        add_operation(event.char)
    elif event.char == '\r':
        calculation()
    elif event.char == '':
        clear()
    elif event.char == '\x08':
        clear_one()
    elif event.char == 'q':
        calculation_square()

block.bind("<Key>", key_pressed)    #Переменная для бинда



def make_digit_button(digit):    #Принимает аргумент цифру
    return tk.Button(text=digit, bd=1, font=('Arial', 25), command=lambda : add_digit(digit))    #return(Подставляет кнопку в атрибут make_operation_btn)

def make_digit2_button(digit):    #Принимает аргумент цифру
    return tk.Button(text=digit, bd=1, font=('Arial', 25))    #return(Подставляет кнопку в атрибут make_operation_btn)

def make_operation_button(operation):    #operation(атрибут производимой операции при нажатии на клавишу удалить)
    return tk.Button(text=operation, bd=1, font=('Arial', 25), fg='#ff9257', command=lambda : add_operation(operation))    #lambda(выполняет вычисление)

def make_calls_button(operation):    #operation(атрибут производимой операции при нажатии на клавишу удалить)
    return tk.Button(text=operation, bd=1, font=('Arial', 25), fg='#ff9257', command=calculation)    #command(передает функцию)    #bd(рамки)    #command=lambda(функция для кнопки)

def make_clear_button(operation):    #operation(атрибут производимой операции при нажатии на клавишу удалить)
    return tk.Button(text=operation, bd=1, font=('Arial', 25), fg='#ff9257', command=clear)    #clear(атрибут для переменной с действием удалить)

def make_clears_button(operation):    #operation(атрибут производимой операции при нажатии на клавишу удалить)
    return tk.Button(text=operation, bd=1, font=('Arial', 25), fg='#ff9257', command=clear_one)    #clear(атрибут для переменной с действием удалить)

def make_square2_button(operation):    #operation(атрибут производимой операции при нажатии на клавишу удалить)
    return tk.Button(text=operation, bd=1, font=('Arial', 25), fg='#ff9257', command=calculation_square)    #clear(атрибут для переменной с действием удалить)

def make_percent_button(operation):    #operation(атрибут производимой операции при нажатии на клавишу удалить)
    return tk.Button(text=operation, bd=1, font=('Arial', 25), fg='#ff9257', command=calculation_percent)    #clear(атрибут для переменной с действием удалить)

def make_dot_button(operation):    #operation(атрибут производимой операции при нажатии на клавишу удалить)
    return tk.Button(text=operation, bd=1, font=('Arial', 25), fg='#ff9257', command=lambda : add_dot(operation))    #lambda(выполняет вычисление)



def add_digit(digit):    #Нажатие кнопок воспроизводится на мониторе калькулятора
    value=bend.get()    #Ввод значения в значении с правой стороны
    if value[0]=='0':    #Если первое значение ноль, то он вырезает его
        value=value[1:]    #Берёт всё кроме первого символа если начинается с нуля
    bend['state']=tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
    bend.delete(0,tk.END)    #Очистка поле вввода при помощи атрибута Delete
    bend.insert(0,value+digit)    #Добавление операции в поле ввода
    bend['state'] = tk.DISABLED    #Блокировка поля ввода

def add_digit2(digit2):    #Нажатие кнопок воспроизводится на мониторе калькулятора
    value=bend.get()    #Ввод значения в значении с правой стороны
    bend['state']=tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
    bend.delete(0,tk.END)    #Очистка поле вввода при помощи атрибута Delete
    bend.insert(0,value+digit2)    #Добавление операции в поле ввода
    bend['state'] = tk.DISABLED    #Блокировка поля ввода

def add_operation(operation):    #Добавление операции
    value=bend.get()    #Ввод значения в значении с правой стороны
    if value [-1] in '.-+/*':    #Проверка значений операции(если это -+/* то это операция заменяется)
        value=value[:-1]    #В случае повтора операции (знаков) то она заменяет операцию если она находится на конце
    bend['state'] = tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
    bend.delete(0,tk.END)    #Очистка поле вввода при помощи атрибута Delete
    bend.insert(0,value+operation)    #Добавление операции в поле ввода
    bend['state'] = tk.DISABLED    #Блокировка поля ввода

def calculation():    #Воспроизведение вычеслений
    value=bend.get()    #команда выполняется дальше если значение не заканчивается на(+-/*)
    if value[-1] in '.+-*/':    #если операция заканчивается на одном из знаков (+-/*)
        value=value+value[:-1]    #операция выполняется в минусовом символе(то есть само на себя)
    bend['state'] = tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
    bend.delete(0, tk.END)    #Очистка поле вввода при помощи атрибута Delete
    try:
        bend.insert(0, eval(value))    #eval(выполняет основные вычисления)
        bend['state'] = tk.DISABLED    #Блокировка поля ввода
    except ZeroDivisionError:    #Атрибут ошибки деления на ноль
        messagebox.showinfo('Ошибка', 'На ноль делить нельзя!')    #Сообщение об ошибке
        bend.insert(0, 0)    #Добавление операции в поле ввода

def calculation_square():
    value = bend.get()    #Команда выполняется дальше если значение не заканчивается на(+-/*)
    if value[-1] in '+-*/':    #Если операция заканчивается на одном из знаков (+-/*)
        value = value + value[:-1]    #Операция выполняется в минусовом символе(то есть само на себя)
    bend['state'] = tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
    bend.delete(0, tk.END)    #Очистка поле вввода при помощи атрибута Delete
    try:
        bend.insert(0, eval(value) ** 2)    #eval(выполняет основные вычисления)
        bend['state'] = tk.DISABLED    #Блокировка поля ввода
    except ZeroDivisionError:    #Атрибут ошибки деления на ноль
        messagebox.showinfo('Ошибка', 'Не корректный ввод!')    #Сообщение об ошибке
        bend.insert(0, 0)    #Добавление операции в поле ввода
        bend['state'] = tk.DISABLED    #Блокировка поля ввода

def calculation_percent():    #Добавление операции процент
    value = bend.get()    #Команда выполняется дальше если значение не заканчивается на(+-/*)
    if value[-1] in '+-*/':    #Если операция заканчивается на одном из знаков (+-/*)
        value = value + value[:-1]    #Операция выполняется в минусовом символе(то есть само на себя)
    bend['state'] = tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
    bend.delete(0, tk.END)    #Очистка поле ввода при помощи атрибута Delete
    try:
        bend['state'] = tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
        bend.insert(0, eval(value) / 100)    #Деление числа на 100(Для выводы процентов)
        bend['state'] = tk.DISABLED    #Блокировка поля ввода
    except ZeroDivisionError:    #Атрибут ошибки
        messagebox.showinfo('Ошибка', 'Не корректный ввод!')
        bend.insert(0, 0)    #Добавление операции в поле ввода
        bend['state'] = tk.DISABLED    #Блокировка поля ввода

def clear():    #Добавление операции "удалить"
    bend['state'] = tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
    bend.delete(0, tk.END)    #Очистка поле вввода при помощи атрибута Delete
    bend.insert(0,0)    #Добавление операции в поле ввода
    bend['state'] = tk.DISABLED    #Блокировка поля ввода

def clear_one():    #Добавление операции "стереть"
    n = bend.get()[0: -1]    #Удаление одного значения
    bend['state'] = tk.NORMAL    #Нормальное состояние ввода текста в поле ввода
    bend.delete(0, tk.END) #Очистка поле вввода при помощи атрибута Delete
    bend.insert(0, n)    #Добавление операции в поле ввода
    if bend.get() == '':    #Вставляет пустоту вместо символа
        bend.insert(0, 0)
    bend['state'] = tk.DISABLED    #Блокировка поля ввода

def add_dot(operation):    #Добавление операции "точка"
    value = bend.get()    #Ввод значения в значении с правой стороны
    if value[-1] in '.+-*/':  #Проверка значений операции(если это -+/* то это операция заменяется)
        value = value[:-1]  #В случае повтора операции (знаков) то она заменяет операцию если она находится на конце
    bend['state'] = tk.NORMAL  #Нормальное состояние ввода текста в поле ввода
    bend.delete(0, tk.END)  #Очистка поле ввода при помощи атрибута Delete
    bend.insert(0, value + operation)  #Добавление операции в поле ввода
    bend['state'] = tk.DISABLED    #Блокировка поля ввода



make_digit_button('1').grid(row=4, column=0, stick='wens')    #Кнопка    #stick(Расширение кнопок по заданным размерам)
make_digit_button('2').grid(row=4, column=1, stick='wens')    #Кнопка    #row(Колонна по вертикали)    #column(Колонна по горизонтали)
make_digit_button('3').grid(row=4, column=2, stick='wens')
make_digit_button('4').grid(row=3, column=0, stick='wens')
make_digit_button('5').grid(row=3, column=1, stick='wens')
make_digit_button('6').grid(row=3, column=2, stick='wens')
make_digit_button('7').grid(row=2, column=0, stick='wens')
make_digit_button('8').grid(row=2, column=1, stick='wens')
make_digit_button('9').grid(row=2, column=2, stick='wens')
make_digit_button('0').grid(row=5, column=1, stick='wens')

make_operation_button('/').grid(row=1, column=3, stick='wens')
make_operation_button('*').grid(row=2, column=3, stick='wens')
make_operation_button('-').grid(row=3, column=3, stick='wens')
make_operation_button('+').grid(row=4, column=3, stick='wens')

make_clear_button('Del').grid(row=1, column=0, stick='wens')
make_clears_button('C').grid(row=1, column=1, stick='wens')

make_square2_button('X^2').grid(row=6, column=2, stick='wens')
make_percent_button('%').grid(row=1, column=2, stick='wens')

make_dot_button('.').grid(row=5, column=3, stick='wens')

make_calls_button('=').grid(row=6, column=3, stick='wens')
make_digit_button('(').grid(row=5, column=0, stick='wens')
make_digit_button(')').grid(row=5, column=2, stick='wens')

make_digit2_button('').grid(row=6, column=0, stick='wens')
make_digit2_button('').grid(row=6, column=1, stick='wens')



block.grid_columnconfigure(0, minsize=90)    #Размер ширины колонны
block.grid_columnconfigure(1, minsize=90)
block.grid_columnconfigure(2, minsize=90)
block.grid_columnconfigure(3, minsize=90)
block.grid_columnconfigure(4, minsize=90)

block.grid_rowconfigure(1, minsize=90)    #Размер высоты колонны
block.grid_rowconfigure(2, minsize=90)
block.grid_rowconfigure(3, minsize=90)
block.grid_rowconfigure(4, minsize=90)
block.grid_rowconfigure(5, minsize=90)
block.grid_rowconfigure(6, minsize=90)

block.mainloop()    #Цикл. Для того чтобы окно не закрывалось