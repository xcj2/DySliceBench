# -*- coding: utf-8 -*-


def insertionSort(A, n, g):
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g

        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v

    return cnt


def shellSort(A, n):
    cnt = 0
    m = 1
    G = []
    while True:
        if n < int((3 ** m - 1) / 2):
            m -= 1
            break
        else:
            G.append(int((3 ** m - 1) / 2))
            m += 1

    G.reverse()

    for i in range(m):
        cnt += insertionSort(A, n, G[i])

    print_line(A, G, m, cnt)


def print_line(A, G, m, cnt):
    print(m)
    for i in range(len(G)):
        if i == len(G) - 1:
            print(G[i])
        else:
            print("{0}".format(G[i]), end=' ')
    print(cnt)
    for i in range(len(A)):
        print(A[i])

A = []
n = int(input())
for i in range(n):
    A.append(int(input()))

shellSort(A, n)
