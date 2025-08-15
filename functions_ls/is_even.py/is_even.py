# -*- coding: cp1251 -*-   #��� �������� ����� � ������

def is_even (number, file_out = None):
    if number % 2 == 0:
        if file_out:
            file_out.write(f"{number} - ������\n")
        else:
            print(f"{number} - ������\n")
    else:
         if file_out:
            file_out.write(f"{number} - ��������\n")
         else:
            print(f"{number} - ��������\n")

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        number = int(input("����������, ������� ����� ��� �������� �� ��������:\n"))
        is_even(number)
    elif choice == 2:
        file_in = open("input.txt", "r")
        number = int(file_in.read())
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        is_even(number, file_out)
        print("��������� ������� � ����� \"output.txt\"\n")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")
