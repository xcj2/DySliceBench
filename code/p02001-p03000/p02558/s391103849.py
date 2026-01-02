#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())

def resolve():
    N, Q = iim()
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

    ans = []
    for t, u, v in zip(it, it, it):
        if t == 1:
            ans.append(1 if find(u) == find(v) else 0)
        else:
            union(u, v)

    print(*ans, sep="\n")


if __name__ == "__main__":
    resolve()
