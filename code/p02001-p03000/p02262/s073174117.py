# -*- coding:utf-8 -*-

import math

def insertion_sort(num_list, length, interval):
    cnt = 0
    for i in range(interval, length):
        v = num_list[i]
        j = i - interval
        while j >= 0 and num_list[j] > v:
            num_list[j+interval] = num_list[j]
            j = j - interval
            cnt = cnt + 1
        num_list[j+interval] = v
    return cnt

def shell_sort(num_list, length):
    cnt = 0
    h = 4
    intervals = [1,]
    while length > h:
        intervals.append(h)
        h = 3 * h + 1
    for i in reversed(range(len(intervals))):
        cnt = cnt + insertion_sort(num_list, length, intervals[i])
    print(len(intervals))
    show_list(intervals)
    print(cnt)

def show_list(list):
    i = len(list) - 1;
    while i > 0:
        print(list[i], end=" ")
        i = i - 1
    print(list[i])

input_num = int(input())
input_list = list()
for i in range(input_num):
    input_list.append(int(input()))
shell_sort(input_list, input_num)
for num in input_list:
    print(num)