import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
from copy import deepcopy 

MAXN = 1005
MAXV = MAXN * (MAXN - 1)//2
G = [[] for _ in range(MAXV)]

id = [[-1] * MAXN for _ in range(MAXN)]
def toId(i,j):
    if i > j:
        i,j = j,i
    return id[i][j]


finished = [0] * MAXV
dp = [-1] * MAXV
def dfs(v):
    if dp[v] != -1:
        if finished[v] == 0:
            return -1
        return dp[v]
    dp[v] = 0
    for e in G[v]:
        res = dfs(e)
        if res == -1:
            return -1
        dp[v] = max(dp[v],res + 1)
    finished[v] = 1
    return dp[v]


def main():
    n = int(input())
    a = [[int(i) - 1 for i in input().split()] for _ in range(n)]

    v = 0
    for i in range(n):
        for j in range(i + 1,n):
            id[i][j] = v
            v += 1
    
    for i in range(n):
        for j in range(n - 1):
            a[i][j] = toId(i,a[i][j])
        for j in range(n - 2):
            G[a[i][j]].append(a[i][j + 1])
    
    ans = 0
    for i in range(v):
        res = dfs(i)
        if res == -1:
            ans = -1
            break
        ans = max(ans,dfs(i) + 1)
    
    print(ans)

if __name__=='__main__':
    main()