import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


#隣接リスト 1-order
def make_adjlist_d(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def main():
    X, Y, A, B, C = NMI()
    P = NLI()
    Q = NLI()
    R = NLI()
    reds = [[1, p] for p in P]
    greens = [[2, q] for q in Q]
    skels = [[0, r] for r in R]
    apples = reds + greens + skels
    apples.sort(key=lambda x: x[1], reverse=True)

    colors = [0, 0, 0]
    limits = [10**9, X, Y]
    ans = 0
    for color, a in apples:
        if sum(colors) >= X + Y:
            break

        if colors[color] <= limits[color] - 1:
            colors[color] += 1
            ans += a
            continue

    print(ans)


if __name__ == "__main__":
    main()