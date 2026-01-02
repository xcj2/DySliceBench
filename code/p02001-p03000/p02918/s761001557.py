# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


def zz():
    return list(map(int, input().split()))


def z():
    return int(input())


def S():
    return input()


def C(line):
    return [input() for _ in range(line)]


N, K = zz()
S = S()
change_points = [0]
if (N == 1):
    print(0)
    exit()
if (S[0] == S[1] == 'R'):
    ans = 1
else:
    ans = 0
for i in range(1, N):
    if S[i] == 'L':
        if (S[i - 1] == 'L'):
            ans += 1
    else:
        if (i == N - 1):
            pass
        elif (S[i + 1] == 'R'):
            ans += 1

    if (S[i] != S[i - 1]):
        change_points.append(i)
# print(change_points)
# print(ans)
ans += (2*K)

print(min(ans, N-1))
