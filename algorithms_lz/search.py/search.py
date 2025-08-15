# -*- coding: cp1251 -*-   #��� �������� ����� � ������

import random #��� ���������� ���������� ������

def line_search (array, element): #�������� �����
    count_of_steps = 0
    n = len(array)
    for i in range(n):
        if array[i] == element:
            return i, count_of_steps #��������� ������� ��� ������ ������� ������ �������
        count_of_steps += 1
    return -1, count_of_steps
    

def binary_search (array, element): #�������� �����
    count_of_steps = 0
    offset = 0 #�������� �������� �� �� ������� ������� �� 2, ������� �� ���� �������� ������
    n = len(array)
    while n > 0:
        count_of_steps += 1
        half = n // 2
        if array[half] == element:
            return offset + half, count_of_steps #��������� ������� ��� ������ ������� ������ �������
        elif array[half] < element:
            array = array[half + 1:]
            offset += half + 1
        else:
            array = array[:half]
        n = len(array)
    return -1, count_of_steps



try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        array = random.sample(range(0, 1000000), 100)
        array.sort()
        print("�������� ��������� � ��������������� ������ �� 100 ��������, � ������� ����� ������������� ����� ���������:\n", array)
        element = int(input("������� ����������� ������� ��� ������:\n"))
        index_by_line_search, count_of_steps_ls = line_search(array, element)
        index_by_binary_search, count_of_steps_bs = binary_search(array, element)
        if index_by_line_search == -1:
            print(f"�������� �����. ������� {element} �� ��� ������\n") 
        else :
            print(f"�������� �����. ������ �������� {element} : {index_by_line_search}\n���������� ����������� ���������: {count_of_steps_ls}\n") 
        if index_by_binary_search == -1:
            print(f"�������� �����. ������� {element} �� ��� ������\n")
        else :
            print(f"�������� �����. ������ �������� {element} : {index_by_line_search}\n���������� ����������� ���������: {count_of_steps_bs}\n")
    elif choice == 2:
        file_in = open("input.txt", "r")
        element = file_in.read()
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        array = random.sample(range(0, 1000000), 100)
        array.sort()
        file_out.write("�������� ��������� � ��������������� ������ �� 100 ��������, � ������� ����� ������������� ����� ��������:\n")
        for i in array:
            file_out.write(f"{i}, " )

        index_by_line_search, count_of_steps_ls = line_search(array, int(element))
        index_by_binary_search, count_of_steps_bs = binary_search(array, int(element))

        if index_by_line_search == -1:
           file_out.write(f"\n�������� �����. ������� {element} �� ��� ������\n") 
        else :
            file_out.write(f"\n�������� �����. ������ �������� {element} : {index_by_line_search}\n")
            file_out.write("\n���������� ����������� ���������:\n") 
            file_out.write(str(count_of_steps_ls))
        if index_by_binary_search == -1:
            file_out.write(f"\n�������� �����. ������� {element} �� ��� ������\n")
        else :
            file_out.write(f"\n������ �������� {element} : {index_by_binary_search}\n")
            file_out.write("\n���������� ����������� ���������:\n") 
            file_out.write(str(count_of_steps_bs))

        print("��������� ������� � ����� \"output.txt\"\n")
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: #���� ��������� ��������� ��� python ���� �� ����� IDE, �� ������� ���������� ����������� ����� ��������. � ��� ����������� ������ ��� ��������
    input("������� Enter, ����� ������� ����...")
