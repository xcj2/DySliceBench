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


def main():
    N = int(input())
    S = input()

    que = deque()
    for s in S:
        if len(que) == 0:
            que.append(s)
        elif que[-1] == "(" and s == ")":
            que.pop()
        else:
            que.append(s)

    d = defaultdict(int)
    while len(que):
        d[que[-1]] += 1
        que.pop()

    print("(" * d[")"] + S + ")" * d["("])


if __name__ == '__main__':
    main()
