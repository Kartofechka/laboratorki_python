# -*- coding: cp1251 -*-   #��� �������� ����� � ������

def convert_time (time):
    return time * 60

def convert_to_seconds (time):
    time_in_hours = int(time[0])
    time_in_minutes = int(time[1]) + convert_time(time_in_hours)
    return int(time[2]) + convert_time(time_in_minutes)

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        time = (input("����������, ������� ����� � ������� ����-������-������� ��� �������� � �������:\n").split("-"))
        print(f"����� � ��������: {convert_to_seconds(time)}\n")
    elif choice == 2:
        file_in = open("input.txt", "r")
        time = (file_in.read().split("-"))
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        file_out.write(f"����� � ��������: {convert_to_seconds(time)}\n")
        print("��������� ������� � ����� \"output.txt\"\n")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")
