# coding: utf-8

def returnInt(x):
    return int(x[-1])

def bubbleSort(A, N):
    flag = 1
    while flag:
        flag = 0
        for i in range(N - 1, 0, -1):
            if returnInt(A[i]) < returnInt(A[i - 1]):
                A[i], A[i - 1] = A[i - 1], A[i]
                flag = 1
    print(' '.join(A))
    return A

def selectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if returnInt(A[j]) < returnInt(A[minj]):
                minj = j
        A[i], A[minj] = A[minj], A[i]
    print(' '.join(A))
    return A

if __name__ == "__main__":
    N = int(input())
    A = input().split()
    B = [i for i in A]

    A_bubble = bubbleSort(A, N)
    print('Stable')
    A_selection = selectionSort(B, N)
    if A_bubble == A_selection:
        print('Stable')
    else:
        print('Not stable')
