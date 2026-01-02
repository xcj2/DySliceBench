import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N, M = geta(int)
    g = defaultdict(lambda: [])
    for _ in range(M):
        x, y = geta(int)
        g[x].append(y)

    dp = [-1] * (N + 1)

    def dfs(i):
        if dp[i] == -1:
            dist = 0
            for j in g[i]:
                dist_j = 1 + dfs(j)
                if dist_j > dist: dist = dist_j
            dp[i] = dist
        return dp[i]

    ans = 0
    for i in range(1, N + 1):
        tmp = dfs(i)
        if tmp > ans: ans = tmp

    print(ans)


if __name__ == "__main__":
    main()