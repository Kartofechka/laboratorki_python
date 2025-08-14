# -*- coding: cp1251 -*-   #��� �������� ����� � ������

def count_of_steps (argument): #������� �������� �� ��������
    if argument % 3 == 0:
        return str(argument // 3)
    else:
        return str(argument // 3 + 1)

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        argument = int(input("����������, ������� ���� ����� ��� ����������� ��������:\n")); #�������� ������ � �������
        if argument < 1 or argument > 100000: #��������� ������ ��������������� ������� �����
            raise Exception("������������ �������� ������ �� ����������!")
        print("����������� ���������� ��������: ", count_of_steps(argument)) #������� ��������� � �������
    elif choice == 2:
        print("������ ����� ������� �� ����� \"input.txt\"\n")
        file_in = open("input.txt", "r")
        argument = int(file_in.read())
        if argument < 1 or argument > 100000: #��������� ������ ��������������� ������� �����
            raise Exception("������������ �������� ������ �� ����������!")
        file_out = open("output.txt", "w") 
        print("��������� ������� � ����� \"output.txt\"\n")
        file_out.write(count_of_steps(argument))
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: #���� ��������� ��������� ��� python ���� �� ����� IDE, �� ������� ���������� ����������� ����� ��������. � ��� ����������� ������ ��� ��������
    input("������� Enter, ����� ������� ����...")
