#!/usr/bin/env python3


def yoko(A):
    f = False
    for i in range(3):
        if len(set(A[i]))==1:f = True
    return f

def tate(A):
    f = False
    for i in range(3):
        B = [A[0][i],A[1][i],A[2][i]]
        if len(set(B))==1: f = True
    return f


def naname(A):
    f = False
    B = [A[0][0],A[1][1],A[2][2]]
    if len(set(B))==1: f = True
    B = [A[0][2], A[1][1], A[2][0]]
    if len(set(B))==1: f = True

    return f


A = []

A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

N = int(input())
for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                A[j][k]=-1

F1 = tate(A)
F2 = yoko(A)
F3 = naname(A)


if F1 or F2 or F3: print('Yes')
else: print('No')


