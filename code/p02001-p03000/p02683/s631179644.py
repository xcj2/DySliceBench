def ad(A, B):
    n = len(A)
    tmp = [0] * n
    for i in range(n):
        tmp[i] += A[i] + B[i]
    return tuple(tmp)

def judge(A):
    flag = True
    for i in A[1:]:
        if i < X:
            flag = False
    return flag

def rec(A, i):
    global ans
    if i == N:
        if judge(A) and ans > A[0]:
            ans = A[0]
        return 0
    rec(ad(A,C[i]), i + 1)
    rec(A, i + 1)

N, M, X = [int(i) for i in input().split()]
C = [[int(i) for i in input().split()] for _ in range(N)]
A = tuple([0]*(M+1))
ans = 12*(10**5) + 1
rec(A, 0)
if ans == 12*(10**5) + 1:
    print(-1)
else:
    print(ans)