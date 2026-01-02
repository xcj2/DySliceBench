def insertionSort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i-1
        while A[j] > v and j >= 0:
            A[j+1], A[j] = A[j], A[j+1]
            j -= 1


def bubbleSort(A, N):
    flag = 1
    while flag:
        flag = 0
        for j in range(N-1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = 1


def bubbleSort_card(C, N):
    flag = 1
    while flag:
        flag = 0
        for j in range(N-1, 0, -1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
                flag = 1

def selectionSort_card(A, N):
    for i in range(N):
        minidx = i
        for j in range(i, N):
            if A[j][1] < A[minidx][1]:
                minidx = j
        A[i], A[minidx] = A[minidx], A[i]

def selectionSort(A, N):
    for i in range(N):
        minidx = i
        for j in range(i, N):
            if A[j] < A[minidx]:
                minidx = j
        A[i], A[minidx] = A[minidx], A[i]


N = int(input())
A = list(input().split())
C = A.copy()
bubbleSort_card(C,N)
selectionSort_card(A,N)
print(" ".join(C))
print('Stable')
print(" ".join(A))
for i in range(N):
    if A[i] != C[i]:
        print('Not stable')
        break
else:
    print('Stable')


