# coding=utf-8
from math import floor, ceil, sqrt, factorial, log, gcd
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement, chain
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heappushpop, heapify
import copy
import sys
INF = float('inf')
mod = 10**9+7
sys.setrecursionlimit(10 ** 6)


def lcm(a, b): return a * b / gcd(a, b)

# 1 2 3
# a, b, c = LI()


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))

# a = I()


def I(): return int(sys.stdin.buffer.readline())

# abc def
# a, b = LS()


def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

# a = S()


def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')

# 2
# 1
# 2
# [1, 2]


def IR(n): return [I() for i in range(n)]

# 2
# 1 2 3
# 4 5 6
# [[1,2,3], [4,5,6]]


def LIR(n): return [LI() for i in range(n)]

# 2
# abc
# def
# [abc, def]


def SR(n): return [S() for i in range(n)]

# 2
# abc def
# ghi jkl
# [[abc,def], [ghi,jkl]]


def LSR(n): return [LS() for i in range(n)]

# 2
# abcd
# efgh
# [[a,b,c,d], [e,f,g,h]]


def SRL(n): return [list(S()) for i in range(n)]


def main():
    h, w = LI()
    grid = SRL(h)
    v = [[-1] * w for i in range(h)]
    v[0][0] = 1
    q = deque()
    q.append((1, 1))

    while q:
        i, j = q.popleft()
        grid[i - 1][j - 1] = "*"
        for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if i + x < 1 or i + x > h or j + y < 1 or j + y > w or grid[i + x - 1][j + y - 1] != "." or v[i + x - 1][j + y - 1] > 0:
                continue
            v[i + x - 1][j + y -
                         1] = v[i - 1][j - 1] + 1
            q.append((i + x, j + y))

    if v[h-1][w-1] < 0:
        print(-1)
        return
    print(h*w-v[h-1][w-1]-list(chain.from_iterable(grid)).count("#"))


if __name__ == "__main__":
    main()
