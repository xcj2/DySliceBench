# coding: utf-8
# クイックソート
import copy


def partition(A, p, r):
    x = int(A[r].split()[1])

    i = p - 1
    tmp = 0

    for j in range(p, r):
        if int(A[j].split()[1]) <= x:
            i = i + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp

    tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp
    return i + 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)
    return (A)


def checkStable(before_list, sorted_list):

    for val in sorted_list:
        same_list = [
            i for i in sorted_list
            if (int(val.split()[1]) == int(i.split()[1])) and val != i
        ]
        if len(same_list) == 0:
            continue

        for data in same_list:
            bef = before_list.index(val) - before_list.index(data)
            aft = sorted_list.index(val) - sorted_list.index(data)

            if (bef > 0 and aft < 0) or (bef < 0 and aft > 0):
                return 'Not stable'

    return 'Stable'


if __name__ == "__main__":
    n = int(input())

    A = []
    for _ in range(n):
        A.append(input())

    bef_A = copy.deepcopy(A)

    aft_A = quickSort(A, 0, n - 1)

    print(checkStable(bef_A, aft_A))

    for data in aft_A:
        print(data)

