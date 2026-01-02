def BubbleSort(N, A):
    for i in range(N):
        flag = True
        while flag:
            flag = False
            for j in range(1, N):
                if int(A[j][1]) < int(A[j - 1][1]):
                    A[j], A[j - 1] = A[j - 1], A[j]
                    flag = True


def SelectionSort(N, A):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        A[i], A[minj] = A[minj], A[i]


def trace(A):
    for i in range(len(A)):
        print(A[i], end='')
        if i != len(A) - 1:
            print(' ', end='')
    print('')


N = int(input())
A = [str(i) for i in input().split()]


A1 = A.copy()

BubbleSort(N, A)
trace(A)
print('Stable')

SelectionSort(N, A1)
trace(A1)

same = True
for i in range(N):
    if A[i] != A1[i]:
        same = False
if same:
    print('Stable')
else:
    print('Not stable')

