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

# データ構造：ヒープ
import heapq
class heapque:
    def __init__(self, *args):
        self.que = []
        for arg in args:
            self.push(arg)
    def push(self, v):
        heapq.heappush(self.que, v)
    def pop(self):
        return heapq.heappop(self.que)

# エントリーポイント
def main():
    N, M = input([int, 2])
    A = input([int, N])

    que = heapque()
    for a in A:
        que.push(-a)
    
    for _ in range(M):
        que.push(-(-que.pop() // 2))

    print(-sum(que.que))
    
    return

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
