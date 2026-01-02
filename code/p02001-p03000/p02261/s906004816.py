import copy

def show(C):
    for i in range(len(C)):
        if i :
            print(' ', end = '')
        print(C[i], end = '')
    print()

def bubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
    show(C)

def SelectionSort(D, N):
    for i in range(N):
        min_j = i
        for j in range(i, N):
            if D[j][1] < D[min_j][1]:
                min_j = j
        D[i], D[min_j] = D[min_j], D[i]
    show(D)

N = int(input())
C = [i for i in input().split()]
D = copy.copy(C)

bubbleSort(C, N)
print('Stable')
SelectionSort(D, N)
if C == D:
    print('Stable')
else:
    print('Not stable')

