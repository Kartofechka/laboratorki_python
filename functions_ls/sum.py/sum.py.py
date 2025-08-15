# -*- coding: cp1251 -*-   #Для русского языка в выводе

def element_is_number(element):
    try:
        float(element)
        return True
    except:
        return False

def sum_of_list(array):
    sum = 0
    for i in array:
        sum += float(i)
    return sum

try: #обработчик для всех исключений не вдаваясь в тип ошибки
    choice = int(input("""Выберете вариант ввода и вывода данных: 
    [1] Работа с консолью
    [2] Работа с файлом\n""")) #Пользователь сам выбирает способ ввода и вывода данных
    if choice == 1: 
        input_list = input("Пожалуйста, введите ваш лист для нахождения суммы чисел через пробел:\n").split()
        list_of_only_numbers = list(filter(element_is_number, input_list))
        print(f"Сумма всех чисел в листе = {sum_of_list(list_of_only_numbers)}")
    elif choice == 2:
        file_in = open("input.txt", "r")
        input_list = file_in.read().split()
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 для вывода текста на русском в файл
        list_of_only_numbers = list(filter(element_is_number, input_list))
        file_out.write(f"Сумма всех чисел в листе = {str(sum_of_list(list_of_only_numbers))}")
        print("Данные записаны в файл \"output.txt\"")
        file_in.close()
        file_out.close()
    else:
        print("Неверный вариант")
except Exception as error:
    print("Что-то пошло не так: ", error)
finally: 
    input("Нажмите Enter, чтобы закрыть окно...")

