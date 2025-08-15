# -*- coding: cp1251 -*-   #Для русского языка в выводе

import math

def square_of_circle (radius):
    return math.pi * float(radius ** 2)

def lenght_of_circle (radius):
    return  math.pi * float(2 * radius)

try: #обработчик для всех исключений не вдаваясь в тип ошибки
    choice = int(input("""Выберете вариант ввода и вывода данных: 
    [1] Работа с консолью
    [2] Работа с файлом\n""")) #Пользователь сам выбирает способ ввода и вывода данных
    if choice == 1: 
        radius = int(input("Пожалуйста, введите радиус круга:\n"))
        print(f"Площадь круга = {square_of_circle(radius)}, длинна окружности = {lenght_of_circle(radius)}\n")
    elif choice == 2:
        file_in = open("input.txt", "r")
        radius = int(file_in.read())
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 для вывода текста на русском в файл
        file_out.write(f"Площадь круга = {square_of_circle(radius)}, длинна окружности = {lenght_of_circle(radius)}\n")
        print("Результат записан в файле \"output.txt\"\n")
        file_in.close()
        file_out.close()
    else:
        print("Неверный вариант")
except Exception as error:
    print("Что-то пошло не так: ", error)
finally: 
    input("Нажмите Enter, чтобы закрыть окно...")
