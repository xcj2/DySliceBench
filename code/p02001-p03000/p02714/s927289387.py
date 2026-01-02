from collections import deque, Counter as cnt
from collections import defaultdict as dd
from operator import itemgetter as ig
from bisect import bisect_right as bsr
from math import factorial, ceil, floor
import sys
sys.setrecursionlimit(1000000)

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
    if not n:
        return [] if type(v) is list else v
    return [nlist(n[1:], v) for _ in range(n[0])]


# エントリーポイント
PARA = {"R": (1, 0, 0), "G": (0, 1, 0), "B": (0, 0, 1)}
PARA2 = {"R": 0, "G": 1, "B": 2}


def main():
    N, S = input(int, str)
    count = [(0, 0, 0)]
    for s in reversed(S):
        left = count[-1]
        count.append(((left[0] + PARA[s][0]),
                      (left[1] + PARA[s][1]),
                      (left[2] + PARA[s][2])))
    count.reverse()
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            if S[i] == S[j]:
                continue
            last = ({"R", "G", "B"} - {S[i], S[j]}).pop()
            ans += count[j + 1][PARA2[last]]
            if ((j * 2 - i < N) and S[j * 2 - i] == last):
                ans -= 1
    print(ans)

    return


if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
