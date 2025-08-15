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

def minimal_number(array):
    minimal = array[0]
    for i in array:
        if i < minimal:
            minimal = i
    return minimal

def maximal_number(array):
    maximal = array[0]
    for i in array:
        if i > maximal:
            maximal = i
    return maximal

def avarage_number(array):
    return sum_of_list(array) / len(array)

def clossest_number_to_avarage(array):
    clossest_number = array[0]
    avarage_num = avarage_number(array)
    minimal_difference = abs(avarage_num - clossest_number)
    for i in array:
        if (abs(avarage_num - i)) < minimal_difference:
            clossest_number = i
            minimal_difference = abs(avarage_num - i)
    return clossest_number

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        input_list = input("����������, ������� ��� ���� ��� ���������� ����� ����� ����� ������:\n").split()
        list_of_only_numbers = [float(x) for x in input_list if element_is_number(x)]
        print(f"""����������� ����� �� ������ = {minimal_number(list_of_only_numbers)}
        ������������ ����� �� ������ = {maximal_number(list_of_only_numbers)}
        ������� ����� ������ = {avarage_number(list_of_only_numbers)}
        ��������� ����� � �������� = {clossest_number_to_avarage(list_of_only_numbers)}
        """)
    elif choice == 2:
        file_in = open("input.txt", "r")
        input_list = file_in.read().split()
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        list_of_only_numbers = [float(x) for x in input_list if element_is_number(x)]
        file_out.write(f"""����������� ����� �� ������ = {minimal_number(list_of_only_numbers)}\n
        ������������ ����� �� ������ = {maximal_number(list_of_only_numbers)}
        ������� ����� ������ = {avarage_number(list_of_only_numbers)}
        ��������� ����� � �������� = {clossest_number_to_avarage(list_of_only_numbers)}
        """)
        print("������ �������� � ���� \"output.txt\"")
        file_in.close()
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: 
    input("������� Enter, ����� ������� ����...")
