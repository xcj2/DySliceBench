def lower_elements(A, b):
    ''' リストAの要素のうち，b未満のものの個数を返す関数 '''
    lower_bound = -1
    upper_bound = len(A)
    while upper_bound - lower_bound > 1:
        middle = (lower_bound + upper_bound) // 2
        if A[middle] < b:
            lower_bound = middle
        else:
            upper_bound = middle
    return lower_bound + 1


def upper_elements(C, b):
    ''' リストCの要素のうち，cより大きいものの個数を返す関数 '''
    i = -1
    j = len(C)
    while j - i > 1:
        m = (i + j) // 2
        if C[m] > b:
            j = m
        else:
            i = m
    return len(C) - j


def answer(N, A, B, C):
    A.sort()
    B.sort()
    C.sort()
    count = 0
    for b in B:
        count += lower_elements(A, b) * upper_elements(C, b)
    return count


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
print(answer(N, A, B, C))
