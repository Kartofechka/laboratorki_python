# -*- coding: cp1251 -*-   #Для русского языка в выводе

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

try: #обработчик для всех исключений не вдаваясь в тип ошибки
    choice = int(input("""Выберете вариант ввода и вывода данных: 
    [1] Работа с консолью
    [2] Работа с файлом\n""")) #Пользователь сам выбирает способ ввода и вывода данных
    if choice == 1: 
        number = int(input("Пожалуйста, введите ваше число для подсчета суммы цифр:\n"))
        print(f"Сумма цифр числа = {sum_of_digits(number)}")
    elif choice == 2:
        file_in = open("input.txt", "r")
        number = int(file_in.read())
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 для вывода текста на русском в файл
        file_out.write(f"Сумма цифр числа = {sum_of_digits(number)}")
        print("Данные записаны в файл \"output.txt\"")
        file_in.close()
        file_out.close()
    else:
        print("Неверный вариант")
except Exception as error:
    print("Что-то пошло не так: ", error)
finally: 
    input("Нажмите Enter, чтобы закрыть окно...")

