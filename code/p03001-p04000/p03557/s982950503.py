def lower(A, b):
    i = -1
    j = len(A)
    while j - i > 1:
        m = (i + j) // 2
        if A[m] < b:
            i = m
        else:
            j = m
    return i + 1


def upper(C, b):
    i = -1
    j = len(C)
    #print('in upper 1', C, b)
    while j - i > 1:
        m = (i + j) // 2
        #print('in upper 2', i, m, j, C[m] > b)
        if C[m] > b:
            j = m
        else:
            i = m
    return len(C) - j


def answer(N, A, B, C):
    A.sort()
    B.sort()
    C.sort()
    #print(A)
    #print(B)
    #print(A)
    count = 0
    for b in B:
        #print(b, lower(A, b), upper(C, b))
        count += lower(A, b) * upper(C, b)
    return count


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
print(answer(N, A, B, C))
