# -*- coding: cp1251 -*-   #��� �������� ����� � ������

def element_is_number(element):
    try:
        float(element)
        return True
    except:
        return False

def sum_of_list(array):
    sum = 0
    for i in array:
        sum += float(i)
    return sum

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        input_list = input("����������, ������� ��� ���� ��� ���������� ����� ����� ����� ������:\n").split()
        list_of_only_numbers = list(filter(element_is_number, input_list))
        print(f"����� ���� ����� � ����� = {sum_of_list(list_of_only_numbers)}")
    elif choice == 2:
        file_in = open("input.txt", "r")
        input_list = file_in.read().split()
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        list_of_only_numbers = list(filter(element_is_number, input_list))
        file_out.write(f"����� ���� ����� � ����� = {str(sum_of_list(list_of_only_numbers))}")
        print("������ �������� � ���� \"output.txt\"")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")

