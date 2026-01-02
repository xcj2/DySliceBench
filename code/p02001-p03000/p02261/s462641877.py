N = int(input())
A = [x for x in input().split()]

B = [int(x[1]) for x in A]
C = [x[0] for x in A]
D = [int(x[1]) for x in A]
E = [x[0] for x in A]
F = [int(x[1]) for x in A]
G = [x[0] for x in A]

def bubbleSort(A, B, N):
    for i in range(0, N):
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                B[j], B[j-1] = B[j-1], B[j]
    return 0

def selectionSort(A, B, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]: minj = j
        A[i], A[minj] = A[minj], A[i]
        B[i], B[minj] = B[minj], B[i]
    return 0

def showArray(A, B, N):
    for _ in range(N):
        if _ == N-1:
            print(A[_], sep='', end='')
            print(B[_], sep='', end='')
        else:
            print(A[_], sep='', end='')
            print(B[_], sep='', end=' ')
    print()
    return 0

def isStable(A, B, C, D, N):
    for _ in range(1, 10):
        if A.count(_) > 1:
            if [B[i] for i, x in enumerate(A) if x == _] == [D[i] for i, x in enumerate(C) if x == _]:
                continue
            else:
                return 'Not stable'
    return 'Stable'

if __name__ == '__main__':
    bubbleSort(B, C, N)
    selectionSort(D, E, N)
    
    showArray(C, B, N)
    print(isStable(B, C, F, G, N))
    showArray(E, D, N)
    print(isStable(D, E, F, G, N))
