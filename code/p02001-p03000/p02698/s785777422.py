#!/usr/bin/env python3

import sys, bisect
sys.setrecursionlimit(300000)


def solve(N: int, a: "List[int]", u: "List[int]", v: "List[int]"):
    conns = [[] for _ in range(N)]
    for i in range(N - 1):
        conns[u[i] - 1].append(v[i] - 1)
        conns[v[i] - 1].append(u[i] - 1)

    ret = [-1] * N
    dp = []
    def dfs(idx):
        val = a[idx]
        k = -1
        if len(dp) == 0 or val > dp[-1]:
            dp.append(val)
        else:
            k = bisect.bisect_left(dp, val)
            tmp = dp[k]
            dp[k] = val
        ret[idx] = len(dp)
        for j in conns[idx]:
            if ret[j] >= 0:
                continue
            dfs(j)

        if k >= 0:
            dp[k] = tmp
        else:
            dp.pop()
        return
    dfs(0)
    for r in ret:
        print(r)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, a, u, v)

if __name__ == '__main__':
    main()
