import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(1000000)


def li_input():
    return [int(_) for _ in input().split()]

def BubbleSort(N, A):

    for i in range(N):
        for j in range(N - 1, i, -1):
            if int(A[j][1]) < int(A[j - 1][1]):
                A[j], A[j - 1] = A[j - 1], A[j]
    
    return A

def SelectionSort(N, A):

    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        
        A[i], A[minj] = A[minj], A[i]
            
    return A

def is_stable(A, A_):
    for i in range(len(A_) - 1):
        if A_[i][1] == A_[i + 1][1]:
            j = A.index(A_[i])
            k = A.index(A_[i + 1])
            
            if j > k:
                return "Not stable"
    
    return "Stable"

def main():
    N = int(input())
    A = input().split()

    BA = BubbleSort(N, A[:])
    SA = SelectionSort(N, A[:])

    print(" ".join(list(map(str, BA))))
    print(is_stable(A, BA))
    print(" ".join(list(map(str, SA))))
    print(is_stable(A, SA))


main()

