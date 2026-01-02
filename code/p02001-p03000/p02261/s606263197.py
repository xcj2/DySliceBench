# -*- coding: utf-8 -*-


def BubbleSort(C, N):
    flag = 1
    while flag == 1:
        flag = 0
        for i in range(N - 1, 0, -1):
            if int(C[i][1]) < int(C[i - 1][1]):
                C[i], C[i - 1] = C[i - 1], C[i]
                flag = 1
    return C


def SelectionSort(C, N):
    flag = 0

    for i in range(N):

        if N == 1:
            break

        minj = i
        for j in range(i, N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
                flag = 1

        if flag == 1:
            C[i], C[minj] = C[minj], C[i]

        flag = 0

    return C


def print_line(A):
    for i in range(len(A)):
        if i == len(A) - 1:
            print('{0}{1}'.format(A[i][0], A[i][1]))
        else:
            print('{0}{1} '.format(A[i][0], A[i][1]), end='')


def check_stable(Bubble_A, Select_A):
    for i in range(len(Select_A)):
        if Bubble_A[i][0] != Select_A[i][0]:
            print('Not stable')
            break
        elif i == len(Select_A) - 1:
            print('Stable')


N = int(input())
A = list(input())

A = [A[i:i+2] for i in range(0, len(A), 3)]

Bubble_A = BubbleSort(A[:], N)
Select_A = SelectionSort(A[:], N)

print_line(Bubble_A)
print('Stable')
print_line(Select_A)
check_stable(Bubble_A, Select_A)

