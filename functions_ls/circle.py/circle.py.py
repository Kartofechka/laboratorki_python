# -*- coding: cp1251 -*-   #��� �������� ����� � ������

import math

def square_of_circle (radius):
    return math.pi * float(radius ** 2)

def lenght_of_circle (radius):
    return  math.pi * float(2 * radius)

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        radius = int(input("����������, ������� ������ �����:\n"))
        print(f"������� ����� = {square_of_circle(radius)}, ������ ���������� = {lenght_of_circle(radius)}\n")
    elif choice == 2:
        file_in = open("input.txt", "r")
        radius = int(file_in.read())
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        file_out.write(f"������� ����� = {square_of_circle(radius)}, ������ ���������� = {lenght_of_circle(radius)}\n")
        print("��������� ������� � ����� \"output.txt\"\n")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")
