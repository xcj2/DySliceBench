# coding: utf-8
# Your code here!

def bubble_sort(A):
    for i in range(len(A)):
        flag = 1
        while flag:
            flag = 0
            for j in range(len(A)-1, i, -1):
                if A[j][1] < A[j-1][1]:
                    A[j], A[j-1] = A[j-1], A[j]
                    flag = 1
    return A

def sentaku_sort(A):
    for i in range(len(A)):
        min_n = i
        for j in range(i+1, len(A)):
            if A[j][1] < A[min_n][1]:
                min_n = j
        if min_n != i:
            A[i], A[min_n] = A[min_n], A[i]
    return A

def isStable(A, B):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            for a in range(len(A)):
                for b in range(a+1, len(A)):
                    if A[i][1] == A[j][1] and A[i] == B[b] and A[j] == B[a]:
                        return False
    return True
    

def hyoji(A):
    for i in range(len(A)):
        if i != len(A)-1:
            print(A[i], end = ' ')
        else:
            print(A[i])


n = int(input())
A = input().split()

B = bubble_sort(A[:])
hyoji(B)
if isStable(A, B):print('Stable')
else:print('Not stable')

C = sentaku_sort(A[:])
hyoji(C)
if isStable(A, C):print('Stable')
else:print('Not stable')

