# -*- coding: utf-8 -*-

class Card:
    def __init__(self, str):
        self.suit  = str[0]
        self.value = int(str[1])

    def __str__(self):
        return self.suit + str(self.value)

def swap(A, i, j):
    tmp  = A[i]
    A[i] = A[j]
    A[j] = tmp

def BubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j].value < C[j-1].value:
                swap(C, j, j-1)  # C[j] と C[j-1] を交換

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j].value < C[minj].value:
                minj = j
        swap(C, i, minj)  # C[i] と C[minj] を交換

def isStable(A, B):
    for i in range(1, len(B)):
        if B[i-1].value == B[i].value:
            for j in range(len(A)):
                if A[j] == B[i-1]: break
                if A[j] == B[i]:   return False
    return True

N = int(input())
A = [Card(t) for t in input().split()]
if len(A) != N: raise

B = A[:]
S = A[:]
BubbleSort(B, N)
SelectionSort(S, N)
print(' '.join(map(str, B)))
print('Stable' if isStable(A, B) else 'Not stable')
print(' '.join(map(str, S)))
print('Stable' if isStable(A, S) else 'Not stable')
