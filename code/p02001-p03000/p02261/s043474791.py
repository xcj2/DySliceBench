# -*- coding:utf-8 -*-

import copy

def bubble_sort(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)-1, i , -1):
            if num_list[j][1] < num_list[j-1][1]:
                num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
    return num_list

def selection_sort(num_list):
    for i in range(len(num_list)):
        mini = i
        for j in range(i, len(num_list)):
            if num_list[j][1] < num_list[mini][1]:
                mini = j
        num_list[i], num_list[mini] = num_list[mini], num_list[i]
    return num_list

def is_stable(before_sort, after_sort):
    current_num = 0
    same_number_card = list()
    for num in after_sort:
        if current_num == int(num[1]):
            for same_card in same_number_card:
                if before_sort.index(same_card) > before_sort.index(num):
                    return False
            same_number_card.append(num)
        else:
            current_num = int(num[1])
            same_number_card = [num,]
    return True

def show_list(list):
    i = 0;
    while(i < len(list)-1):
        print(list[i], end=" ")
        i = i + 1
    print(list[i])

def show_stable(flag):
    if flag:
        print('Stable')
    else:
        print('Not stable')

num = int(input())
input_card = [x for i, x in enumerate(input().split()) if i < num]
bubble_sort_card = bubble_sort(copy.deepcopy(input_card))
show_list(bubble_sort_card)
show_stable(is_stable(input_card, bubble_sort_card))
selection_sort_card = selection_sort(copy.deepcopy(input_card))
show_list(selection_sort_card)
show_stable(is_stable(input_card, selection_sort_card))