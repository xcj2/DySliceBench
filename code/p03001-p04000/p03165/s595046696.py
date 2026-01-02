def main():
    from bisect import bisect_left as bl, bisect_right as br, insort
    import sys
    import heapq
    # from math import *
    from collections import defaultdict as dd, deque
    def data():
        return sys.stdin.readline().strip()

    def mdata():
        return map(int, data().split())

    out = sys.stdout.write
    # sys.setrecursionlimit(100000)
    INF = int(10e9)

    s = data()
    t = data()
    dp = [[0] * (len(s) + 1) for i in range(len(t) + 1)]
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if s[j - 1] == t[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    m = max(max(dp))
    ans = ''
    for i in range(len(t) - 1, -1, -1):
        for j in range(len(s) - 1, -1, -1):
            if dp[i + 1][j + 1] == m and s[j] == t[i]:
                ans = s[j] + ans
                m -= 1
                break
    out(ans+'\n')


if __name__ == '__main__':
    main()