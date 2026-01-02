# Aizu Problem ALDS_1_2_C: Stable Sort
#
import sys, math, os

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input2.txt", "rt")


def printA(A):
    print(' '.join([str(a) for a in A]))


def bubble_sort(A):
    for i in range(len(A) - 1):
        for j in range(len(A) - 1, i, -1):
            if A[j][1] < A[j - 1][1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A

def selection_sort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[j][1] < A[mini][1]:
                mini = j
        if mini != i:
            A[i], A[mini] = A[mini], A[i]
    return A

def is_stable(A, B):
    for val in range(1, 10):
        v = str(val)
        if [a[0] for a in A if a[1] == v] != [b[0] for b in B if b[1] == v]:
            return False
    return True
        
N = int(input())
A = list(input().split())
A_bubble = bubble_sort(A[:])
printA(A_bubble)
print("Stable" if is_stable(A, A_bubble) else "Not stable")
A_select = selection_sort(A[:])
printA(A_select)
print("Stable" if is_stable(A, A_select) else "Not stable")