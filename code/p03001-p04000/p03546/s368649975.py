import sys
sys.setrecursionlimit(10**9)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
'''
def check(A):
    num = A[1]
    for i in range(10):
        if A[i] >= num and i!=1:
            A[i] = INF
    print('check', A)
    for i in range(10):
        if A[i]!=INF and A[i]!=0 and i!=1:
                return True
    return False


def dfs(A):
    k = check(A)
    while k:
        for i in range(10):
            if i!= 1 and A[i] != INF:
                for j in range(10):
                    if A[j] != INF:
                        A[j] = min(A[i]+C[i][j], A[j])
                        if j == 1 and A[j]==A[i]+C[i][j]:
                            A[i] = INF
        print('dfs', A)
        k = check(A)
    print(A)
    return A[1]

    

H, W = mi()
C = li2(10)
a = li2(H)
ans = 0

INF = 10**9
memo = [INF]*10

for i in range(10):
    if i!= 1:
        A = []
        for j in range(10):
            A.append(C[i][j])
        print(A)
        memo[i] = dfs(A)
        print(i, memo[i])

for i in range(H):
    for j in range(W):
        if a[i][j] != -1 and a[i][j] != 1:
            ans += memo[a[i][j]]

print(memo)

print(ans)
'''
H, W = mi()
C = li2(10)
a = li2(H)
memo = [C[i][1] for i in range(10)]
flag = -1

def dfs(column, m):
    #print('a')
    if column == 1:
        global flag
        flag = max(m, flag)
    for i in range(10):
        if i!=column and C[column][i] < m:
            dfs(i, m-C[column][i])
    return False

for i in range(10):
    if i != 1:
        dfs(i, C[i][1])
        #print(flag)
        if flag != -1:
            memo[i] = C[i][1]-flag
            #print(i, flag)
        flag = -1
    #print(memo)

ans = 0

for i in range(H):
    for j in range(W):
        if abs(a[i][j]) != 1:
            ans += memo[a[i][j]]
#print(memo)
print(ans)