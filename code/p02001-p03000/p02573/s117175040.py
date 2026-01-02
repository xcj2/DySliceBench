#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    N, M = iim()
    it = map(int, sys.stdin.read().split())

    dp = [-1] * N

    def find(x):
        if dp[x] < 0:
            return  x

        ans = dp[x] = find(dp[x])
        return ans

    def union(x, y):
        x1 = find(x)
        y1 = find(y)

        if x1 == y1:
            return

        xr = dp[x1]
        yr = dp[y1]
        if xr <= yr:
            dp[y1] = x1
            dp[x1] += yr
        else:
            dp[x1] = y1
            dp[y1] += xr

    for ai, bi in zip(it, it):
        union(ai-1, bi-1)

    d1 = [0]*N
    for i in range(N):
        d1[find(i)] += 1
    print(max(d1))

if __name__ == "__main__":
    resolve()
