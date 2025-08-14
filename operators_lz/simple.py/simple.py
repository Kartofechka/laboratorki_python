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
        argument = int(input("����������, ������� ���� ����� ��� ����������� ��������:\n")); #�������� ������ � �������
        if argument < 1 or argument > 25: #��������� ������ ��������������� ������� �����
            raise Exception("������������ �������� ������ �� ����������!")
        print("��������� ����������� �������� �����: ", is_simple(argument)) #������� ��������� � �������
    elif choice == 2:
        print("������ ����� ������� �� ����� \"input.txt\"\n")
        file_in = open("input.txt", "r")
        argument = int(file_in.read())
        if argument < 1 or argument > 100000: #��������� ������ ��������������� ������� �����
            raise Exception("������������ �������� ������ �� ����������!")
        file_out = open("output.txt", "w") 
        print("��������� ������� � ����� \"output.txt\"\n")
        file_out.write(is_simple(argument))
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: #���� ��������� ��������� ��� python ���� �� ����� IDE, �� ������� ���������� ����������� ����� ��������. � ��� ����������� ������ ��� ��������
    input("������� Enter, ����� ������� ����...")
