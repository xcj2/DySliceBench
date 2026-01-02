import copy
def bubbleSort(A, N):
    cnt = 0
    flag = 1
    while flag:
        flag = 0
        for j in range(N - 1, 0, -1):
            if A[j][1] < A[j - 1][1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = 1
                cnt = cnt + 1
    return cnt
 
 
def selectionSort(A, N):
    cnt = 0
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j][1] < A[minj][1]:
                minj = j
        cnt = cnt + int(i != minj)
        A[i], A[minj] = A[minj], A[i]
    return cnt
 
def prArr(A, N):
    for i in range(N):
        if i != 0:
            print(" ", end = "")
        print(A[i], end = "")
    print()
 
     
N = int(input())
A = [i for i in input().split()]
B = copy.deepcopy(A)
 
bubbleSort(A, N)
selectionSort(B, N)
 
prArr(A, N)
print("Stable")
 
prArr(B, N)
print("Stable" if A == B else "Not stable")
