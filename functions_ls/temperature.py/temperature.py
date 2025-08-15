# -*- coding: cp1251 -*-   #��� �������� ����� � ������

def converting_temperature (temperature):
    return float(temperature) * 1.8 + 32

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        temperature = int(input("����������, ������� ����������� � �������� �������:\n"))
        print(f"����������� �� ���������� = {converting_temperature(temperature)}\n")
    elif choice == 2:
        file_in = open("input.txt", "r")
        temperature = int(file_in.read())
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        file_out.write(f"����������� �� ���������� = {converting_temperature(temperature)}\n")
        print("��������� ������� � ����� \"output.txt\"\n")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")
