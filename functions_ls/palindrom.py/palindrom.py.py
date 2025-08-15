# -*- coding: cp1251 -*-   #Для русского языка в выводе

def is_palindrom(line):
    if line == line[::-1]: #Сравниваем исходную строку и развернутую строку
        return True
    else:
        return False


try: #обработчик для всех исключений не вдаваясь в тип ошибки
    choice = int(input("""Выберете вариант ввода и вывода данных: 
    [1] Работа с консолью
    [2] Работа с файлом\n""")) #Пользователь сам выбирает способ ввода и вывода данных
    if choice == 1: 
        line = input("Пожалуйста, введите вашу строку для проверки на полиндром:\n")
        if is_palindrom(line):
            print(f"Строка является полиндромом")
        else:
            print(f"Строка не является полиндромом")
    elif choice == 2:
        file_in = open("input.txt", "r")
        line = file_in.read()
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 для вывода текста на русском в файл
        if is_palindrom(line):
            file_out.write(f"Строка является полиндромом")
        else:
            file_out.write(f"Строка не является полиндромом")
        print("Данные записаны в файл \"output.txt\"")
        file_in.close()
        file_out.close()
    else:
        print("Неверный вариант")
except Exception as error:
    print("Что-то пошло не так: ", error)
finally: 
    input("Нажмите Enter, чтобы закрыть окно...")
