# coding:utf-8

import sys
from collections import defaultdict, deque

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n, k = LI()

    G = defaultdict(list)
    AB = [LI_() for _ in range(n - 1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)

    def DFS(ss: list, t: int):
        q = deque()
        for s in ss:
            q.append((s, 0))
        visited = [0] * n
        visited[ss[0]] = visited[ss[-1]] = 1
        while q:
            v, d = q.pop()
            if d >= t:
                continue
            for to in G[v]:
                if visited[to]:
                    continue
                visited[to] = 1
                q.append((to, d + 1))
        
        return n - sum(visited)

    # 木の性質
    # 直径をdとした時
    # dが偶数ならば，ある頂点vから他の頂点への距離がD/2となる頂点vが存在する
    # dが奇数ならば，ある辺eから他の頂点への距離が(D-1)/2となる辺eが存在する
    res = INF
    if k % 2:
        for a, b in AB:
            res = min(res, DFS([a, b], (k - 1) // 2))
    else:
        for i in range(n):
            res = min(res, DFS([i], k // 2))

    return res


print(main())
