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


n, k = LI()
# n = [int(x) for x in str(n)]
d = set(LI())
notd = list(set(range(10)) - d)
q = deque()
q.appendleft(0)
cnt = 0
ans = []
num = []

# while q:
#     now = q.popleft()
#     cnt += 1
#     if cnt > len(n):
#         ans.append(int("".join(list(map(str, num)))))
#         num = []
#         cnt = 0

#         continue
#     for x in notd:
#         if now in notd:
#             continue
#         num.append(x)
#         q.appendleft(x)

# print(min([x for x in ans if x >= n]))
limit = 11*n
while n < limit:
    flg = 1
    for x in list(str(n)):
        if int(x) in d:
            flg = 0
            break
    if flg:
        print(n)
        break
    n += 1
