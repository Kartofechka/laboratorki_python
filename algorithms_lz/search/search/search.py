# -*- coding: cp1251 -*-   #Для русского языка в выводе

import random #Для рандомного заполнения списка

def line_search (array, element): #Линейный поиск
    count_of_steps = 0
    n = len(array)
    for i in range(n):
        if array[i] == element:
            return i, count_of_steps #Завершаем функцию как только находим нужный элемент
        count_of_steps += 1
    return -1, count_of_steps
    

def binary_search (array, element): #Бинарный поиск
    count_of_steps = 0
    offset = 0 #Значение смещения из за деления массива на 2, которое не даст потерять индекс
    n = len(array)
    while n > 0:
        count_of_steps += 1
        half = n // 2
        if array[half] == element:
            return offset + half, count_of_steps #Завершаем функцию как только находим нужный элемент
        elif array[half] < element:
            array = array[half + 1:]
            offset += half + 1
        else:
            array = array[:half]
        n = len(array)
    return -1, count_of_steps



try: #обработчик для всех исключений не вдаваясь в тип ошибки
    choice = int(input("""Выберете вариант ввода и вывода данных: 
    [1] Работа с консолью
    [2] Работа с файлом\n""")) #Пользователь сам выбирает способ ввода и вывода данных
    if choice == 1: 
        array = random.sample(range(0, 1000000), 100)
        array.sort()
        print("Рандомно созданный и отсортированный массив из 100 значений, в котором будет производиться поиск эллемента:\n", array)
        element = int(input("Введите необходимый элемент для поиска:\n"))
        index_by_line_search, count_of_steps_ls = line_search(array, element)
        index_by_binary_search, count_of_steps_bs = binary_search(array, element)
        if index_by_line_search == -1:
            print(f"Линейный поиск. Элемент {element} не был найден\n") 
        else :
            print(f"Линейный поиск. Индекс элемента {element} : {index_by_line_search}\nКоличество выполненных сравнений: {count_of_steps_ls}\n") 
        if index_by_binary_search == -1:
            print(f"Линейный поиск. Элемент {element} не был найден\n")
        else :
            print(f"Бинарный поиск. Индекс элемента {element} : {index_by_line_search}\nКоличество выполненных сравнений: {count_of_steps_bs}\n")
    elif choice == 2:
        file_in = open("input.txt", "r")
        element = file_in.read()
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 для вывода текста на русском в файл
        array = random.sample(range(0, 1000000), 100)
        array.sort()
        file_out.write("Рандомно созданный и отсортированный массив из 100 значений, в котором будет производиться поиск элемента:\n")
        for i in array:
            file_out.write(f"{i}, " )

        index_by_line_search, count_of_steps_ls = line_search(array, int(element))
        index_by_binary_search, count_of_steps_bs = binary_search(array, int(element))

        if index_by_line_search == -1:
           file_out.write(f"\nЛинейный поиск. Элемент {element} не был найден\n") 
        else :
            file_out.write(f"\nЛинейный поиск. Индекс элемента {element} : {index_by_line_search}\n")
            file_out.write("\nКоличество выполненных сравнений:\n") 
            file_out.write(str(count_of_steps_ls))
        if index_by_binary_search == -1:
            file_out.write(f"\nБинарный поиск. Элемент {element} не был найден\n")
        else :
            file_out.write(f"\nИндекс элемента {element} : {index_by_binary_search}\n")
            file_out.write("\nКоличество выполненных сравнений:\n") 
            file_out.write(str(count_of_steps_bs))

        print("Результат записан в файле \"output.txt\"\n")
        file_out.close()
    else:
        print("Неверный вариант")
except Exception as error:
    print("Что-то пошло не так: ", error)
finally: #если запускать программу как python файл не через IDE, то консоль мнгновенно закрывается после открытия. А эта конструкция решает эту проблему
    input("Нажмите Enter, чтобы закрыть окно...")
