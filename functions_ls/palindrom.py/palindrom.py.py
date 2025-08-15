# -*- coding: cp1251 -*-   #��� �������� ����� � ������

def is_palindrom(line):
    if line == line[::-1]: #���������� �������� ������ � ����������� ������
        return True
    else:
        return False


try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        line = input("����������, ������� ���� ������ ��� �������� �� ���������:\n")
        if is_palindrom(line):
            print(f"������ �������� �����������")
        else:
            print(f"������ �� �������� �����������")
    elif choice == 2:
        file_in = open("input.txt", "r")
        line = file_in.read()
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        if is_palindrom(line):
            file_out.write(f"������ �������� �����������")
        else:
            file_out.write(f"������ �� �������� �����������")
        print("������ �������� � ���� \"output.txt\"")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")
