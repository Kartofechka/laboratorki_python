# -*- coding: cp1251 -*-   #Для русского языка в выводе

import random #Для рандомного заполнения списка

def bubble_sort (array, file_out = None): #Сортировка пузырьком
    count_of_steps = 0
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                count_of_steps += 1
        if file_out: #Выводим данные в файл
            file_out.write("\nТекущее состояние списка (пузырек):\n")
            for element in array:
                file_out.write(f"{element}, ")
            file_out.write("\n")
        else: #Вывод в консоль
            print("\nТекущее состояние списка (пузырек):\n", array)
        if not swapped: #Если не было изменений, то список отсортирован и его дальнейшая проверка не нужна
            break
    return count_of_steps
    

def sort_by_selection (array, file_out = None): #Сортировка выбором
    count_of_steps = 0
    n = len(array)
    for i in range(n):
        index_of_maximal_element = i
        for j in range(i + 1, n):
            if array[index_of_maximal_element] < array[j]:
                index_of_maximal_element = j
            array[i], array[index_of_maximal_element] = array[index_of_maximal_element], array[i]
            count_of_steps += 1
        if file_out: #Выводим данные в файл
            file_out.write("\nТекущее состояние списка (выбором):\n")
            for element in array:
                file_out.write(f"{element}, ")
            file_out.write("\n")
        else: #Вывод в консоль
            print("\nТекущее состояние списка (выбором):\n", array)
    return count_of_steps

def input_random_nums_in_array (array): #Рандомное заполнение массива
    for i in range(100):
        array.append(random.randint(0, 1000000))
    return array

try: #обработчик для всех исключений не вдаваясь в тип ошибки
    choice = int(input("""Выберете вариант ввода и вывода данных: 
    [1] Работа с консолью
    [2] Работа с файлом\n""")) #Пользователь сам выбирает способ ввода и вывода данных
    if choice == 1: 
        array = []
        input_random_nums_in_array(array)
        not_sorted_array = array.copy()
        print("Рандомно созданный массив из 100 значений, который будет отсортирован:\n", array)
        count_of_steps_bs = bubble_sort(array)
        count_of_steps_ss = sort_by_selection(array)
        print("Отсортированный массив пузырьком:\n", array, "\nКоличество выполненных сравнений (сортировка пузырьком):\n", count_of_steps_bs)
        print("Отсортированный массив выбором:\n", array, "\nКоличество выполненных сравнений (сортировка выбором):\n", count_of_steps_ss )
    elif choice == 2:
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 для вывода текста на русском в файл
        array = []
        input_random_nums_in_array(array)
        not_sorted_array = array.copy()
        file_out.write("Рандомно созданный массив из 100 значений, который будет отсортирован:\n")
        for i in array:
            file_out.write(f"{i}, " )

        count_of_steps_bs = bubble_sort(array, file_out)
        count_of_steps_ss = sort_by_selection(not_sorted_array, file_out)

        file_out.write("Отсортированный массив пузырьком:\n")
        for i in array:
            file_out.write(f"{i}, " )
        file_out.write("\nКоличество выполненных сравнений (сортировка пузырьком):\n") 
        file_out.write(str(count_of_steps_bs))

        file_out.write("\nОтсортированный массив выбором:\n")
        for i in not_sorted_array:
            file_out.write(f"{i}, " )
        file_out.write("\nКоличество выполненных сравнений (сортировка выбором):\n") 
        file_out.write(str(count_of_steps_ss))

        print("Результат записан в файле \"output.txt\"\n")
        file_out.close()
    else:
        print("Неверный вариант")
except Exception as error:
    print("Что-то пошло не так: ", error)
finally: #если запускать программу как python файл не через IDE, то консоль мнгновенно закрывается после открытия. А эта конструкция решает эту проблему
    input("Нажмите Enter, чтобы закрыть окно...")
