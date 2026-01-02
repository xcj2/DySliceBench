# coding=utf-8
from math import floor, ceil, sqrt, factorial, log, gcd
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
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
    s = S()
    t = S()
    ans = ""
    flg = 1

    if len(t) > len(s):
        print("UNRESTORABLE")
        return

    for i in range(len(s) - len(t), -1, -1):
        flg = 1
        clipped = s[i:i+len(t)]
        for j in range(len(t)):
            if clipped[j] != t[j] and clipped[j] != "?":
                flg = 0
                break
        if flg:
            ans = s[:i].replace("?", "a") + t + \
                s[i + len(t):].replace("?", "a")
            break

    if not flg:
        print("UNRESTORABLE")
        return
    print(str(ans))


if __name__ == "__main__":
    main()
