import copy

N = int(input())

def hoge(arg):
    return [arg[0], int(arg[1])]

A = list(map(hoge, map(str, input().split())))
A1 = copy.deepcopy(A)
A2 = copy.deepcopy(A)

def bsort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]

def ssort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N, 1):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]

def judge(A, A1):
    for i in range(len(A) - 1):
        if A1[i][1] != A1[i+1][1]:
            continue
        a = A.index(A1[i])
        b = A.index(A1[i+1])
        if a > b:
            return 'Not stable'
    return 'Stable'

def toString(A):
    return A[0] + str(A[1])

bsort(A1, N)
print(' '.join(list(map(toString, A1))))
print(judge(A, A1))
ssort(A2, N)
print(' '.join(list(map(toString, A2))))
print(judge(A, A2))

