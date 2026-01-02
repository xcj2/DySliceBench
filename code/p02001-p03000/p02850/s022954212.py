from collections import defaultdict, deque, Counter
import sys
import bisect
import heapq
import math

# input = sys.stdin.readline

sys.setrecursionlimit(1000000000)

MIN = -10 ** 9
MOD = 10 ** 9 + 7

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def keta(n):
    if n < 10:
        return 1
    return math.floor(math.log10(n - 1)) + 1


def check(A, B, X, n):
    return A * n + B * keta(n) <= X


def main():
    N = int(input())
    ab = [[int(a) - 1 for a in input().split()] for _ in range(N - 1)]

    tree = defaultdict(list)
    # res = {}

    for i, (a, b) in enumerate(ab):
        # aa = tt[a]
        # aa.append((b, i))
        # tt[a] = aa
        if a not in tree:
            tree[a] = []
        tree[a].append((b, i))

    # def p(tt, parent):
    #     children = tt[parent]
    #     res[parent]=children
    #     # res = {parent: children}
    #     for c, ii in children:
    #         p(tt, c)
    #     return res
    #
    #
    # tree = p(tt, 0)

    colors = len(tree[0])
    for k, v in tree.items():
        if k == 0:
            continue
        colors = max(colors, len(v) + 1)

    print(colors)

    res = [None] * (N - 1)

    def solve(pos, parentcol):
        children = tree[pos]
        for iii, (c, i) in enumerate(children):
            res[i] = (parentcol + 1 + iii) % colors
            solve(c, res[i])

    solve(0, -1)

    for i in range(N - 1):
        print(res[i] + 1)


if __name__ == '__main__':
    main()
