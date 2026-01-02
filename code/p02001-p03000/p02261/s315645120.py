# -*- coding: utf-8 -*-


def conv_input(arr):
    ret = []
    for e in arr:
        ret.append((e[0], int(e[1])))
    return ret


def conv_output(conv_arr):
    ret = []
    for e in conv_arr:
        ret.append(e[0] + str(e[1]))
    return ret


def is_stable(arr1, arr2):
    ret = 'Stable'
    for a1, a2 in zip(arr1, arr2):
        if a1 == a2:
            continue
        else:
            ret = 'Not stable'
            break
    return ret


def bubble_sort(n, arr):
    flag = True
    while flag:
        flag = False
        for i in reversed(range(n)):
            if i is 0:
                break
            if arr[i][1] < arr[i - 1][1]:
                tmp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = tmp
                flag = True
    return arr


def selection_sort(n, arr):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if arr[j][1] < arr[minj][1]:
                minj = j
        if i != minj:
            tmp = arr[minj]
            arr[minj] = arr[i]
            arr[i] = tmp
    return arr

if __name__ == '__main__':
    n = int(input())
    arr1 = arr2 = [str(s) for s in input().split()]
    arr1 = conv_output(bubble_sort(n, conv_input(arr1)))
    print(' '.join(map(str, arr1)))
    print('Stable')
    arr2 = conv_output(selection_sort(n, conv_input(arr2)))
    print(' '.join(map(str, arr2)))
    print(is_stable(arr1, arr2))