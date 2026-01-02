#!/usr/bin/env python3
import sys
from collections import defaultdict
from functools import lru_cache
from collections import deque


sys.setrecursionlimit(10**8)
INF = float("inf")

MOD = 1000000007  # type: int


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, src, dest, w=1):
        self.E[src].append((dest, w))
        self.E[dest].append((src, w))


@lru_cache(maxsize=None)
def div(a, b):
    return (a * pow(b, MOD-2, MOD)) % MOD


class Combination(object):

    def __init__(self, N, mod=MOD):
        fac, finv, inv = [0]*(N+1), [0]*(N+1), [0]*(N+1)
        fac[:2] = 1, 1
        finv[:2] = 1, 1
        inv[1] = 1
        for i in range(2, N+1):
            fac[i] = fac[i-1]*i % mod
            inv[i] = -inv[mod % i]*(mod//i) % mod
            finv[i] = finv[i-1]*inv[i] % mod
        self.N = N
        self.MOD = mod
        self.fac = fac
        self.finv = finv
        self.inv = inv

    @lru_cache(maxsize=None)
    def __call__(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        b = (self.finv[k]*self.finv[n-k] % self.MOD)
        return (self.fac[n] * b) % self.MOD


def solve(N: int, a: "List[int]", b: "List[int]"):
    # print(div(3, 2))

    # 全方位木DPをやるぞ！
    # 1. 木DPによって頂点ごとにhogeを求める
    # 2. 木DPで求めたhogeを使って、上手く求める

    # グラフの構築
    g = Graph(N)
    for aa, bb in zip(a, b):
        g.add_edge(aa-1, bb-1)

    # 組み合わせの初期化
    cmb = Combination(N)

    dp = [1]*N                  # 節点vを根とした部分木の塗り方dp[v]
    size = [0]*N                # 節点vを根とした部分木のサイズsize[v]+1

    # 木DPを行うDFS
    queue = [(0, -1)]
    seen = [False]*N

    while queue:
        v, p = queue[-1]
        flag = True
        if seen[v] is False:
            for u, _ in g.E[v]:
                if u == p:
                    continue
                if seen[u] is False:
                    queue.append((u, v))
                    flag = False
        if flag is True:
            # 処理
            for u, _ in g.E[v]:
                if u == p:
                    continue
                size[v] += size[u]+1
                dp[v] *= cmb(size[v], size[u]+1)
                dp[v] %= MOD
                dp[v] *= dp[u]
                dp[v] %= MOD
            # print(v, p)
            queue.pop()
            seen[v] = True
    # print(*queue)
    # print(*[(d, s) for d, s in zip(dp, size)])

    # 節点0には木の根としての値を求めた。
    # 0以外の節点には部分木の根としての値を求めた。
    # 木の根としての値を求めた節点を親としてもつ節点は、自身を木の根とした値を求めることができる

    # 全方位木DPを行うBFS
    queue = deque()
    queue.append((0, -1))

    while len(queue) > 0:
        v, p = queue.popleft()
        for u, _ in g.E[v]:
            if u == p:
                continue
            d = div(dp[v], cmb(N-1, size[u]+1))
            d = div(d, dp[u])
            dp[u] *= cmb(N-1, size[u])
            dp[u] %= MOD
            dp[u] *= d
            dp[u] %= MOD
            queue.append((u, v))

    for v in dp:
        print(v)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)


if __name__ == '__main__':
    main()
