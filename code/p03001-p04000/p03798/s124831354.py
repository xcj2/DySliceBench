from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def ok(last, first, S):
    N = len(S)
    ans = [None] * N
    ans[-1], ans[0] = last, first

    for i in range(N):

        if ans[i] == 0:
            if S[i] == "o":
                nex = ans[i - 1]
            else:
                nex = 1 - ans[i - 1]
        else:
            if S[i] == "o":
                nex = 1 - ans[i - 1]
            else:
                nex = ans[i - 1]

        if ans[(i + 1) % N] is None:
            ans[(i + 1) % N] = nex
        else:
            if ans[(i + 1) % N] != nex:
                return None
    return ans


def main():
    N = int(input())
    S = input()

    for l, f in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        ans = ok(l, f, S)
        if ans is not None:
            print(*["S" if v == 0 else "W" for v in ans], sep="")
            return
    print(-1)


if __name__ == '__main__':
    main()
