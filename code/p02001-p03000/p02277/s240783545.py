#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Input:
6
D 3
H 2
D 1
S 3
D 2
C 1

Output:
Not stable / Stable
D 1
C 1
D 2
H 2
D 3
S 3
"""
import sys
import copy


def partition(_array, start, end):
    x = int(_array[end][2:])
    i = start - 1
    assert start <= end
    for j in range(start, end):
        if int(_array[j][2:]) <= x:
            i += 1
            _array[i], _array[j] = _array[j], _array[i]
    _array[i + 1], _array[end] = _array[end], _array[i + 1]
    return i + 1


def quick_sort(_array, start, end):
    if start < end:
        cursor = partition(_array, start, end)
        quick_sort(_array, start, cursor - 1)
        quick_sort(_array, cursor + 1, end)
    return _array


def merge(_array, left, mid, right):
    array_left = _array[left:mid] + ['N ' + str(int(1e9 + 1))]
    array_right = _array[mid:right] + ['N ' + str(int(1e9 + 1))]

    i, j = 0, 0

    for k in range(left, right):
        if int(array_left[i][2:]) <= int(array_right[j][2:]):
            _array[k] = array_left[i]
            i += 1
        else:
            _array[k] = array_right[j]
            j += 1

    return None


def merge_sort(_array, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(_array, left, mid)
        merge_sort(_array, mid, right)
        merge(_array, left, mid, right)
    return _array


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    array = list(map(lambda x: x.strip(), _input[1:]))
    # assert len(array) == array_length

    merge_array = copy.deepcopy(array)
    merge_result = merge_sort(_array=merge_array, left=0, right=array_length)
    # print(*merge_result, sep='\n')
    quick_result = quick_sort(_array=array, start=0, end=array_length - 1)

    if quick_result != merge_result:
        print('Not stable')
    else:
        print('Stable')
    print(*quick_result, sep='\n')