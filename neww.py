from tkinter import *

# Шестнадцатиричная
def h():
    a = var.get()
    answer = hex(a)[2:]
    hex_output.set(answer)  # Устанавливаем текст в переменной

# Восьмиричная
def o():
    a = var.get()
    answer = oct(a)[2:]
    oct_output.set(answer)  # Устанавливаем текст в переменной

# Двоичная
def b():
    a = var.get()
    answer = bin(a)[2:]
    bin_output.set(answer)  # Устанавливаем текст в переменной

tk = Tk()
tk.title("Преобразователь чисел")

# Поле ввода
var = IntVar()
Label(tk, text="Введите число:").grid(row=0, column=0)
e_input = Entry(tk, textvariable=var)  # Поле ввода для числа
e_input.grid(row=0, column=1)

# Для вывода результатов
hex_output = StringVar()
oct_output = StringVar()
bin_output = StringVar()

Label(tk, text="16-ричное:").grid(row=2, column=0)
Label(tk, textvariable=hex_output).grid(row=2, column=1)

Label(tk, text="8-ричное:").grid(row=3, column=0)
Label(tk, textvariable=oct_output).grid(row=3, column=1)

Label(tk, text="2-ричное:").grid(row=4, column=0)
Label(tk, textvariable=bin_output).grid(row=4, column=1)

# Кнопки перевода
btn_h = Button(tk, text="16-ричное", command=h)
btn_h.grid(row=1, column=0)

btn_o = Button(tk, text="8-ричное", command=o)
btn_o.grid(row=1, column=1)

btn_b = Button(tk, text="2-ричное", command=b)
btn_b.grid(row=1, column=2)

tk.mainloop()
