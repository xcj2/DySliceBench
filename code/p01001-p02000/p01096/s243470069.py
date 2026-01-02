import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def ti(): return tuple(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for _ in range(j)] for _ in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from itertools import accumulate #list(accumulate(A))

## DP

def solve(N):
    A = ti()
    dp = dp2(0, N, N)

    for i in range(N-1):
        if abs(A[i]-A[i+1]) < 2:
            dp[i][i+1] = 2
    
    for h in range(2, N): #hは(区間の長さ)-1
        for i in range(N):
            if i+h >= N:
                break
            j = i+h
            # 区間の長さが偶数の場合
            if h % 2:
                if abs(A[i]-A[j]) < 2 and dp[i+1][j-1] == h-1:
                    dp[i][j] = h + 1
                    continue
                else:
                    dp[i][j] = max(tuple(dp[i][k]+dp[k+1][j] for k in range(i, j)))
            # 区間の長さが奇数の場合
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        else:
            continue

    print(dp[0][N-1])

while True:
    N = ii()
    if N == 0:
        exit()
    solve(N)
