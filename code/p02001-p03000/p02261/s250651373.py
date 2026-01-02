from sys import stdin
from copy import deepcopy
input = stdin.readline

N = int(input())
A = list(input().split())

B = deepcopy(A)
S = deepcopy(A)


def p(N):
    for i in range(len(N)):
        if i == len(N) - 1:
            print(N[i])
        else:
            print(N[i], end=" ")


def bubblesort(n):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if B[j][1] < B[j - 1][1]:
                B[j], B[j - 1] = B[j - 1], B[j]

    p(B)
    print("Stable")


def sellectionsort(n):
    for i in range(N):
        m = i
        for j in range(i + 1, N):
            if S[j][1] < S[m][1]:
                m = j
        S[m], S[i] = S[i], S[m]

    p(S)

    flag = True
    for i in range(N):
        if B[i] != S[i]:
            flag = False

    if flag:
        print("Stable")
    else:
        print("Not stable")


bubblesort(N)
sellectionsort(N)

