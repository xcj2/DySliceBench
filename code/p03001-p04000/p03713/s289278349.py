import sys
from math import factorial, ceil, floor
from bisect import bisect_right as bsr
from operator import itemgetter as ig
from collections import defaultdict as dd
from collections import deque

# お約束
args = None
INF = float("inf")
MOD = int(1e9 + 7)
def input(*ps):
    if type(ps[0]) is list:
        return [input(*ps[0][0]) for _ in range(ps[0][1])]
    elif len(ps) == 1:
        return ps[0](next(args))
    else:
        return [p(next(args)) for p in ps]

# エントリーポイント
def main():
    H, W = input([[int], 2])

    def solve(a_max, b_max):
        min_diff = INF
        for a in range(a_max):
            # 横分割
            area1 = (a * b_max
                    , b_max // 2 * (a_max - a)
                    , (b_max // 2 + b_max % 2) * (a_max - a))
            # 縦分割
            area2 = (a * b_max
                    , (a_max - a) // 2 * b_max
                    , ((a_max - a) // 2 + (a_max - a) % 2) * b_max)
            min_diff = min(min_diff, max(area1) - min(area1), max(area2) - min(area2))
        return min_diff
    print(min(solve(H, W), solve(W, H)))

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
