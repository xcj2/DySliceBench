N = int(input())
C1 = input().split()
C2 = [i for i in C1]


def cVal(s):
    return int(s[1])


def BubbleSort(C, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if cVal(C[j]) < cVal(C[j - 1]):
                C[j], C[j - 1] = C[j - 1], C[j]


def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if cVal(C[j]) < cVal(C[minj]):
                minj = j
        C[i], C[minj] = C[minj], C[i]


def isStable(C1, C2):
    for i1, i2 in zip(C1, C2):
        if i1 != i2:
            return False
    return True

BubbleSort(C1, N)
print(' '.join(C1))
print('Stable')

SelectionSort(C2, N)
print(' '.join(C2))
ans = 'Stable' if isStable(C1, C2) else 'Not stable'
print(ans)
