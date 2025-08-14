# -*- coding: cp1251 -*-   #Для русского языка в выводе

def count_of_steps (argument): #Функция проверки на простоту
    if argument % 3 == 0:
        return str(argument // 3)
    else:
        return str(argument // 3 + 1)

try: #обработчик для всех исключений не вдаваясь в тип ошибки
    choice = int(input("""Выберете вариант ввода и вывода данных: 
    [1] Работа с консолью
    [2] Работа с файлом\n""")) #Пользователь сам выбирает способ ввода и вывода данных
    if choice == 1: 
        argument = int(input("Пожалуйста, введите ваше число для определения простоты:\n")); #Получаем данные с консоли
        if argument < 1 or argument > 100000: #Аргументы должны соответствовать условию задчи
            raise Exception("Недопустимое значение одного из аргументов!")
        print("Необходимое количество операций: ", count_of_steps(argument)) #Выводим результат в консоль
    elif choice == 2:
        print("Данные будут считаны из файла \"input.txt\"\n")
        file_in = open("input.txt", "r")
        argument = int(file_in.read())
        if argument < 1 or argument > 100000: #Аргументы должны соответствовать условию задчи
            raise Exception("Недопустимое значение одного из аргументов!")
        file_out = open("output.txt", "w") 
        print("Результат записан в файле \"output.txt\"\n")
        file_out.write(count_of_steps(argument))
        file_in.close()
        file_out.close()
    else:
        print("Неверный вариант")
except Exception as error:
    print("Что-то пошло не так: ", error)
finally: #если запускать программу как python файл не через IDE, то консоль мнгновенно закрывается после открытия. А эта конструкция решает эту проблему
    input("Нажмите Enter, чтобы закрыть окно...")
