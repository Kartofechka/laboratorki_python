# -*- coding: cp1251 -*-   #��� �������� ����� � ������

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        number = int(input("����������, ������� ���� ����� ��� �������� ����� ����:\n"))
        print(f"����� ���� ����� = {sum_of_digits(number)}")
    elif choice == 2:
        file_in = open("input.txt", "r")
        number = int(file_in.read())
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        file_out.write(f"����� ���� ����� = {sum_of_digits(number)}")
        print("������ �������� � ���� \"output.txt\"")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")

