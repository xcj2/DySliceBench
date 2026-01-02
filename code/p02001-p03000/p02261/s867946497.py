from typing import Any,Sequence
import  copy


def selectionSort(A:Sequence, N:int) -> None:

    for i in range(0, N - 1):
        minj = i
        for j in range(i + 1, N):
            if A[j][1] < A[minj][1]:
                minj = j

        A[i], A[minj] = A[minj], A[i]



def bubble_sort(A:Sequence, N:int) -> None:

    for i in range(N):
        for j in range(N - 1, i, -1):
            if A[j][1] < A[j -1][1]:

                A[j], A[j - 1] = A[j - 1], A[j]


def bool_isStable(C1:Sequence, C2:Sequence, N:int) -> bool:
    for i in range(N):
        if C1[i] != C2[i]:
            return False
    return  True


n = int(input())
B = list(map(str, input().split()))
C1 = n * []
C2 = n * []

C1 = copy.copy(B)
C2 = copy.copy(B)


bubble_sort(C1, n)
selectionSort(C2, n)


print(' '.join(map(str, C1)))
print('Stable')


print(' '.join(map(str, C2)))
if bool_isStable(C1, C2, n) == True:
    print('Stable')
else:
    print('Not stable')

