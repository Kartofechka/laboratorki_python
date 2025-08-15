# -*- coding: cp1251 -*-   #��� �������� ����� � ������

import random #��� ���������� ���������� ������

def bubble_sort (array, file_out = None): #���������� ���������
    count_of_steps = 0
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                count_of_steps += 1
        if file_out: #������� ������ � ����
            file_out.write("\n������� ��������� ������ (�������):\n")
            for element in array:
                file_out.write(f"{element}, ")
            file_out.write("\n")
        else: #����� � �������
            print("\n������� ��������� ������ (�������):\n", array)
        if not swapped: #���� �� ���� ���������, �� ������ ������������ � ��� ���������� �������� �� �����
            break
    return count_of_steps
    

def sort_by_selection (array, file_out = None): #���������� �������
    count_of_steps = 0
    n = len(array)
    for i in range(n):
        index_of_maximal_element = i
        for j in range(i + 1, n):
            if array[index_of_maximal_element] < array[j]:
                index_of_maximal_element = j
            array[i], array[index_of_maximal_element] = array[index_of_maximal_element], array[i]
            count_of_steps += 1
        if file_out: #������� ������ � ����
            file_out.write("\n������� ��������� ������ (�������):\n")
            for element in array:
                file_out.write(f"{element}, ")
            file_out.write("\n")
        else: #����� � �������
            print("\n������� ��������� ������ (�������):\n", array)
    return count_of_steps

def input_random_nums_in_array (array): #��������� ���������� �������
    for i in range(100):
        array.append(random.randint(0, 1000000))
    return array

try: #���������� ��� ���� ���������� �� �������� � ��� ������
    choice = int(input("""�������� ������� ����� � ������ ������: 
    [1] ������ � ��������
    [2] ������ � ������\n""")) #������������ ��� �������� ������ ����� � ������ ������
    if choice == 1: 
        array = []
        input_random_nums_in_array(array)
        not_sorted_array = array.copy()
        print("�������� ��������� ������ �� 100 ��������, ������� ����� ������������:\n", array)
        count_of_steps_bs = bubble_sort(array)
        count_of_steps_ss = sort_by_selection(array)
        print("��������������� ������ ���������:\n", array, "\n���������� ����������� ��������� (���������� ���������):\n", count_of_steps_bs)
        print("��������������� ������ �������:\n", array, "\n���������� ����������� ��������� (���������� �������):\n", count_of_steps_ss )
    elif choice == 2:
        file_out = open("output.txt", "w", encoding="utf-8") #utf-8 ��� ������ ������ �� ������� � ����
        array = []
        input_random_nums_in_array(array)
        not_sorted_array = array.copy()
        file_out.write("�������� ��������� ������ �� 100 ��������, ������� ����� ������������:\n")
        for i in array:
            file_out.write(f"{i}, " )

        count_of_steps_bs = bubble_sort(array, file_out)
        count_of_steps_ss = sort_by_selection(not_sorted_array, file_out)

        file_out.write("��������������� ������ ���������:\n")
        for i in array:
            file_out.write(f"{i}, " )
        file_out.write("\n���������� ����������� ��������� (���������� ���������):\n") 
        file_out.write(str(count_of_steps_bs))

        file_out.write("\n��������������� ������ �������:\n")
        for i in not_sorted_array:
            file_out.write(f"{i}, " )
        file_out.write("\n���������� ����������� ��������� (���������� �������):\n") 
        file_out.write(str(count_of_steps_ss))

        print("��������� ������� � ����� \"output.txt\"\n")
        file_out.close()
    else:
        print("�������� �������")
except Exception as error:
    print("���-�� ����� �� ���: ", error)
finally: #���� ��������� ��������� ��� python ���� �� ����� IDE, �� ������� ���������� ����������� ����� ��������. � ��� ����������� ������ ��� ��������
    input("������� Enter, ����� ������� ����...")
