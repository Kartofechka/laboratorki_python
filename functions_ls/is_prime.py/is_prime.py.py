# -*- coding: cp1251 -*-   #��� �������� ����� � ������

def is_simple (argument): #������� �������� �� ��������
    if argument == 1: return 'N' #1 �� �������
    if argument == 2: return 'Y'
    if argument % 2 == 0: return 'N' 
    for i in range(3, int(argument**0.5) + 1, 2): #��������� ������� � 3 � ������ ��������, �.�. 2 � ������ ��� �������.
        if argument % i == 0: return 'N'
    return 'Y'

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        number = int(input("����������, ������� ����� ��� �������� �� ��������:\n"))
        if is_simple(number):
            print(f"����� {number} - �������\n")
        else:
            print(f"����� {number} - ���������\n")
    elif choice == 2:
        file_in = open("input.txt", "r")
        number = int(file_in.read())
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        if is_simple(number):
            file_out.write(f"����� {number} - �������\n")
        else:
            file_out.write(f"����� {number} - ���������\n")
        print("��������� ������� � ����� \"output.txt\"\n")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")
