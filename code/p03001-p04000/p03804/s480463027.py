# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
import math
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


N, M = zz()
A = [S() for i in range(N)]
B = [S() for i in range(M)]


def check(lis_a, lis_b):
    for a, b in zip(lis_a, lis_b):
        # print(a, b)
        if (a != b):
            return False
    return True


for i in range(N - M+1):
    for j in range(N-M+1):
        ok = 0
        for line in range(M):
            # print(A[i+line][j:j+M], B[line])
            if (A[i+line][j:j+M] != B[line]):
                break
            else:
                ok += 1
        if (ok == M):
            print('Yes')
            exit()
print('No')
