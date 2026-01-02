import math
import collections
import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def main():
    n = int(input())
    maxv = n*(n-1)//2
    a = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        for j in range(n-1):
            a[i][j] -= 1

    v = 0  # 頂点数
    # 頂点にIDをふる
    Id = [[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:  # 1-3 ,2-4など　3-1はダメ
                Id[i][j] = v
                v += 1

    def toId(i, j):
        if i > j:
            i, j = j, i
        return Id[i][j]

    # 頂点間の辺を貼る
    e = [[] for i in range(maxv)]
    for i in range(n):
        for j in range(n - 1):
            a[i][j] = toId(i, a[i][j])
        for j in range(n - 2):
            e[a[i][j + 1]].append(a[i][j])

    # トポロジカルソート
    calculated = [False for i in range(maxv)]
    dp = [-1 for i in range(maxv)]

    def dfs(v):
        if dp[v] != -1:  # サイクル検知
            if not calculated[v]:
                return -1
            return dp[v]
        dp[v] = 1
        for u in e[v]:
            ret = dfs(u)
            if ret == -1:
                return -1
            dp[v] = max(dp[v], ret + 1)
        calculated[v] = True
        return dp[v]

    ans = 0
    for i in range(v):
        ret = dfs(i)
        if ret == -1:  # detected cycle
            print(-1)
            exit()
        ans = max(ans, ret)
    print(ans)


if __name__ == '__main__':
    main()
