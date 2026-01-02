def main():

    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import heapq
    # from math import *
    from collections import defaultdict as dd, deque
    def data(): return sys.stdin.readline().strip()
    def mdata(): return list(map(int, data().split()))
    out = sys.stdout.write
    # sys.setrecursionlimit(100000)
    INF = int(1e9)
    mod = int(1e9)+7

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        dpsum = [0] * (k + 2)
        for l in range(k + 1):
            dpsum[l + 1] = dpsum[l] + dp[i][l]
            dpsum[l + 1] %= mod
        for j in range(k + 1):
            dp[i + 1][j] = (dpsum[j + 1] - dpsum[max(0, j - a[i])]) % mod
    print(dp[n][k])
    
if __name__ == '__main__':
    main()