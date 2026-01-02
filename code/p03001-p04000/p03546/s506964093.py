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

H, W = mi()
C = li2(10)
a = li2(H)
memo = [C[i][1] for i in range(10)]
'''
tmp = -1
def dfs(column, m):
    if column == 1:
        global tmp
        tmp = max(m, tmp)
    for i in range(10):
        if i != column and C[column][i] < m:
            dfs(i, m-C[column][i])
    #return

for i in range(10):
    if i != 1:
        dfs(i, C[i][1])
        if tmp != -1:
            memo[i] = C[i][1] - tmp
        tmp = -1
'''
INF = 10**9
tmp = 10**9
'''
def dfs(col, m):
    if col == 1:
        global tmp
        tmp = min(m, tmp)
    for i in range(10):
        if i != col and m + C[col][i] < lim:
            dfs(i, m + C[col][i])

for i in range(10):
    if i != 1:
        tmp = INF
        lim = C[i][1]
        dfs(i, 0)
        memo[i] = min(tmp, memo[i])
'''
from collections import deque
for i in range(10):
    que = deque()
    lim = C[i][1]
    for j in range(10):
        if C[i][j] < lim:
            que.append([j, C[i][j]])
    while que != deque():
        #print(que)
        k = que.popleft()
        for j in range(10):
            if C[k[0]][j] + k[1] < lim and k[0] != j:
                if j == 1:
                    memo[i] = min(memo[i], C[k[0]][j] + k[1])
                else:
                    que.append([j, C[k[0]][j] + k[1]])

ans = 0
for i in range(H):
    for j in range(W):
        if abs(a[i][j]) != 1:
            ans += memo[a[i][j]]

print(ans)