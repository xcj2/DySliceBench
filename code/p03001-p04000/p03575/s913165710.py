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


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def dfs(i, g, used, ng):
    for j in g[i]:
        if not used[j]:
            if (i, j) == ng or (j, i) == ng:
                continue
            used[j] = True
            dfs(j, g, used, ng)


def main():
    N, M = map(int, input().split())
    g = defaultdict(list)
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        g[a].append(b)
        g[b].append(a)
        edges.append((a, b))

    ans = 0
    for edge in edges:
        used = [False] * N
        used[0] = True
        dfs(0, g, used, edge)
        if False in used:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
