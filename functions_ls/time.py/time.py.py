# -*- coding: cp1251 -*-   #Для русского языка в выводе

def convert_time (time):
    return time * 60

def convert_to_seconds (time):
    time_in_hours = int(time[0])
    time_in_minutes = int(time[1]) + convert_time(time_in_hours)
    return int(time[2]) + convert_time(time_in_minutes)

try: #обработчик для всех исключений не вдаваясь в тип ошибки
    choice = int(input("""Выберете вариант ввода и вывода данных: 
    [1] Работа с консолью
    [2] Работа с файлом\n""")) #Пользователь сам выбирает способ ввода и вывода данных
    if choice == 1: 
        time = (input("Пожалуйста, введите время в формате часы-минуты-секунды для перевода в секунды:\n").split("-"))
        print(f"Время в секундах: {convert_to_seconds(time)}\n")
    elif choice == 2:
        file_in = open("input.txt", "r")
        time = (file_in.read().split("-"))
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 для вывода текста на русском в файл
        file_out.write(f"Время в секундах: {convert_to_seconds(time)}\n")
        print("Результат записан в файле \"output.txt\"\n")
        file_in.close()
        file_out.close()
    else:
        print("Неверный вариант")
except Exception as error:
    print("Что-то пошло не так: ", error)
finally: 
    input("Нажмите Enter, чтобы закрыть окно...")
