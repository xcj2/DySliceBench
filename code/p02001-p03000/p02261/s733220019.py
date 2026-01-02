def swap(a, i, j):
    k = a[j]
    a[j] = a[i]
    a[i] = k


def bubbleSort(A, N):
    flag = True
    while flag:
        flag = False
        for j in reversed(range(1, N)):
            if A[j][1] < A[j-1][1]:
                swap(A, j, j-1)
                flag = True


def selectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j][1] < A[minj][1]:
                minj = j
        swap(A, i, minj)


N = int(input())
A = list(input().split())
B = A[:]

bubbleSort(A, N)
print(*A)
print("Stable")
selectionSort(B, N)
print(*B)
if A == B:
    print("Stable")
else:
    print("Not stable")

