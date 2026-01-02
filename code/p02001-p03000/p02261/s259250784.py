import copy


def bubble_sort(n, A):
    for i in range(n):
        for j in reversed(range(i, n - 1)):
            if A[j + 1][1] < A[j][1]:
                A[j + 1], A[j] = A[j], A[j + 1]
    print(*A)


def selection_sort(n, B):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if B[j][1] < B[minj][1]:
                minj = j
        if minj > i:
            B[i], B[minj] = B[minj], B[i]
    print(*B)


def is_stable(C, S):
    result = "Stable"
    for i in range(1, 10):
        c = [n for n in C if str(i) in n]
        s = [n for n in S if str(i) in n]
        if not c == s:
            result = "Not stable"
            break
    print(result)


n = int(input())
A = input().split()
B = copy.copy(A)
C = copy.copy(A)
bubble_sort(n, A)
is_stable(C, A)
selection_sort(n, B)
is_stable(C, B)


