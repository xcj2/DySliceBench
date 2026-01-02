#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from itertools import chain
from functools import reduce
from collections import OrderedDict, Counter, deque
import operator


def IA(): return [int(x) for x in input().split()]


def IM(N): return [IA() for _ in range(N)]


N = int(input())
B = IA()

sys.setrecursionlimit(500)


def f(b, n):
    if n == 0:
        return []
    for i, x in enumerate(b, 1):
        if i < x or n < x:
            return None
    for i, x in enumerate(b, 1):
        if i == x:
            ret = f(tuple(b[:i-1] + b[i:]), n-1)
            if ret is not None:
                return ret + [i]
    return None


ans = f(B, N)
if ans:
    print(*ans, sep="\n")
else:
    print(-1)
