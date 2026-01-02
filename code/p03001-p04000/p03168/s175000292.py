def main():
    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import heapq
    # from math import *
    from collections import defaultdict as dd, deque
    def data(): return input()
    def mdata(): return map(float, data().split())
    out = sys.stdout.write
    # sys.setrecursionlimit(100000)
    INF = int(1e9)
    mod = int(1e9) + 7

    n = int(data())
    P = list(mdata())
    dp = [0.0] * (n // 2 + 2)
    dp[1] = float(1)
    for i in range(n):
        p=P[i]
        for j in range(len(dp) - 1, 0, -1):
            dp[j] = dp[j - 1] * (1 - p) + dp[j] * (p)
    print(sum(dp))

if __name__ == '__main__':
    main()