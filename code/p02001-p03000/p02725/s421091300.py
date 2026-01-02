# coding: UTF-8
import os

def remove_empty(target_list: list):
    empty_removed_list = [x for x in target_list if x]
    return empty_removed_list


def get_stdin_str_list(input_str=None):
    if input_str is None:
        input_str = input()
    input_str = input_str.strip()
    input_str_list = input_str.split()
    return input_str_list


def get_stdin_int_list(input_str=None):
    input_str_list = get_stdin_str_list(input_str)
    input_int_list = list(map(int, input_str_list))
    return input_int_list


def get_stdin_str_multi_list(input_str=None):
    if input_str is None:
        input_str = input()
    input_str = input_str.strip()
    input_str_line_list = input_str.split("\n")
    input_str_multi_list = list()
    for str_line in input_str_line_list:
        input_str_list = get_stdin_str_list(str_line)
        input_str_multi_list.append(input_str_list)
    return input_str_multi_list


def get_stdin_int_multi_list(input_str=None):
    input_str_multi_list = get_stdin_str_multi_list(input_str)
    input_int_multi_list = list()
    for str_list in input_str_multi_list:
        input_int_list = list(map(int, str_list))
        input_int_multi_list.append(input_int_list)
    return input_int_multi_list

def get_most_far_pos_index_from_both_neighbors(pos_list, end_pos_distance=None):
    if end_pos_distance is None:
        end_pos_distance = pos_list[-1]
    N = len(pos_list)
    max_distance = 0
    most_far_pos_index = 0
    for i, p in enumerate(pos_list):
        if i == 0:
            distance = end_pos_distance - pos_list[-1] + pos_list[i+1]
        elif i == N-1:
            distance = end_pos_distance - pos_list[i-1] + pos_list[0]
        else:
            distance = pos_list[i+1] - pos_list[i-1]
        
        if distance > max_distance:
            max_distance = distance
            most_far_pos_index = i

    return most_far_pos_index

def get_longest_interval(pos_list, end_pos_distance=None):
    if end_pos_distance is None:
        end_pos_distance = pos_list[-1]
    N = len(pos_list)
    longest_interval = 0

    for i, p in enumerate(pos_list):
        if i == N-1:
            pos_n_1 = end_pos_distance + pos_list[0]
        else:
            pos_n_1 = pos_list[i+1]

        interval = pos_n_1 - p

        if interval > longest_interval:
            longest_interval = interval

    return longest_interval

K, N = get_stdin_int_list()
A = get_stdin_int_list()
longest_interval = get_longest_interval(A, K)
shortest_distance = K - longest_interval
print(shortest_distance)