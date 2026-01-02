import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

sys.setrecursionlimit(10**8)

#メモ化再帰
def rec(x):
    global dp
    if dp[x]!=-1:
        return dp[x]
    num = 0
    for a in adj[x]:
        num = max(num, rec(a)+1)
    dp[x] = num
    return num

#入力受け取り
N, M = mi()
x = li2(M)

#隣接リスト作成
adj = [[] for i in range(N)]
for i in range(M):
    x[i][0] -= 1
    x[i][1] -= 1
    adj[x[i][0]].append(x[i][1])

#メモ化再帰を実行
dp = [-1]*N
for i in range(N):
    rec(i)

print(max(dp))
