import copy

def bubbleSort(A, N):
    count = 0
    for i in range(1, N):
        for j in reversed(range(i, N)):
            if A[j][1] < A[j-1][1]:
                A[j], A[j-1] = A[j-1], A[j]
                count += 1

def selectionSort(A, N):
    count = 0
    for i in range(N):
        min = i
        for j in range(i, N):
            if A[j][1] < A[min][1]:
                min = j
        if min != i:
            A[i], A[min] = A[min], A[i]
            count += 1

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

