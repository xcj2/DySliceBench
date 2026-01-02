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


def partition(array, start, end):
    x = int(array[end][2:])
    i = start - 1
    assert start <= end
    for j in range(start, end):
        if int(array[j][2:]) <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def quick_sort(array, start, end):
    if start < end:
        cursor = partition(array, start, end)
        quick_sort(array, start, cursor - 1)
        quick_sort(array, cursor + 1, end)
    return array


def merge(A, left, mid, right):
    L = A[left:mid] + ['N ' + str(int(1e9 + 1))]
    R = A[mid:right] + ['N ' + str(int(1e9 + 1))]

    i, j = 0, 0

    for k in range(left, right):
        if int(L[i][2:]) <= int(R[j][2:]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    return None


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)
    return A


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    array_length = int(_input[0])
    array = list(map(lambda x: x.strip('\n'), _input[1:]))
    assert len(array) == array_length

    merge_array = copy.deepcopy(array)

    # print('merge',merge_array)
    merge_result = merge_sort(A=merge_array, left=0, right=array_length)
    # print(*merge_result, sep='\n')

    # print('quick',array)
    quick_result = quick_sort(array=array, start=0, end=array_length - 1)
    if quick_result != merge_result:
        print('Not stable')
    else:
        print('Stable')
    print(*quick_result, sep='\n')