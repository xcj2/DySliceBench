def bubbleSort(A):
    N = len(A)
    for i in range(N):
        for j in range(N - 1, i, -1):
            if A[j][1] < A[j - 1][1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A


def selectionSort(A):
    N = len(A)
    for i in range(N):
        min_i = i
        for j in range(i, N):
            if A[j][1] < A[min_i][1]:
                min_i = j
        if min_i != i:
            A[i], A[min_i] = A[min_i], A[i]
    return A


def is_stable(A, B):
    for i in range(len(B) - 1):
        if B[i][1] == B[i + 1][1]:
            if A.index(B[i]) > A.index(B[i + 1]):
                return False
    return True


N = int(input())
A = list(input().split())

B = bubbleSort(A[:])
print(*B)
if is_stable(A, B):
    print('Stable')
else:
    print('Not stable')

S = selectionSort(A[:])
print(*S)
if is_stable(A, S):
    print('Stable')
else:
    print('Not stable')