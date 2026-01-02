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
    N, K, Q = input([int, 3])
    A = input([int, Q])

    ps = [0] * (N + 1)
    max_p = 0
    for a in A:
        ps[a] += 1
        max_p = max(max_p, ps[a])
    
    for p in ps[1:]:
        if p <= (Q - K):
            print("No")
        else:
            print("Yes")
    return

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
