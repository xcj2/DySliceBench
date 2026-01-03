from _collections import deque


def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()


def gw():
    global input_parser
    return next(input_parser)


def gi():
    data = gw()
    return int(data)


MOD = int(1e9 + 7)

import numpy
from collections import deque
from math import sqrt
from math import floor
#https://atcoder.jp/contests/arc081/tasks/arc081_b
#D - Coloring Dominoes
"""
need to consider the case that ticket is not enough to lower everything
"""

N = gi()
x = gi()
A = [0] * N

for i in range(N):
    A[i] = gi()

ans = 0
if (A[0] > x):
    ans += A[0] - x
    A[0] = x

for i in range(1, N):
    diff = A[i] + A[i - 1] - x
    if diff > 0:
        cost = min(diff, A[i])
        A[i] -= cost
        ans += cost

    diff = A[i] + A[i - 1] - x
    if diff > 0:
        cost -= min(diff, A[i - 1])
        A[i - 1] -= cost
        ans += cost
print(ans)
