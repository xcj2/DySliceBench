import sys
sys.setrecursionlimit(1000000)
from math import factorial, ceil, floor
from bisect import bisect_right as bsr
from operator import itemgetter as ig
from collections import defaultdict as dd
from collections import deque, Counter as cnt

# お約束
args = None
INF = float("inf")
MOD = int(1e9 + 7)
def input(*ps):
    if type(ps[0]) is list:
        return [input(*ps[0][:-1]) for _ in range(ps[0][-1])]
    elif len(ps) == 1:
        return ps[0](next(args))
    else:
        return [p(next(args)) for p in ps]
def nlist(n, v):
    if not n: return [] if type(v) is list else v
    return [nlist(n[1:], v) for _ in range(n[0])]

# エントリーポイント
def main():
    N, M = input(int, int)
    ABC = input([[int, 3], M])

    # Nから到達できる辺のみ抽出する
    g = nlist([N + 1], [])
    for a, b, c in ABC:
        g[b] += [(a, c)]

    que, rch = [N], {N}
    while que:
        cur = que.pop()
        for nxt, _ in g[cur]:
            if nxt in rch: continue
            rch |= {nxt}
            que.append(nxt)
    edges = [(a, b, c) for a, b, c in ABC if a in rch and b in rch]

    # ベルマンフォード法で負の最短経路(スコアの最大値)を導出する
    g = nlist([N + 1], INF)
    g[1] = 0
    for _ in range(N):
        f = True
        for a, b, c in edges:
            c = -c
            if g[a] + c < g[b]:
                g[b] = g[a] + c
                f = False
        if f:
            break
    else:
        # 負の閉路を除外する
        print("inf")
        return
    print(-g[N])
    return

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
