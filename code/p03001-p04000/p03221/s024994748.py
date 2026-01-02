from __future__ import print_function

from functools import reduce
from operator import mul
from collections import Counter
from collections import deque
from itertools import accumulate
from queue import Queue
from queue import PriorityQueue as pq
from heapq import heapreplace
from heapq import heapify
from heapq import heappushpop
from heapq import heappop
from heapq import heappush
import heapq
import time
import random
import bisect
import itertools
import collections
from fractions import Fraction
import fractions
import string
import math
import operator
import functools
import copy
import array
import re
import sys
sys.setrecursionlimit(500000)


input = sys.stdin.readline


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    return


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def cmp_vec(u, v):
    if u[1] < v[1]:
        return -1
    elif u[1] == v[1]:
        if u[2] < v[2]:
            return -1
        elif u[2] == v[2]:
            return 0
        else:
            return 1
    else:
        return 1


def main():
    #
    n, m = map(int, input().strip().split())
    l = []
    for i in range(m):
        p, y = map(int, input().strip().split())
        p = str(p).zfill(6)
        l.append(list((i, p, y)))
    l.sort(key=functools.cmp_to_key(cmp_vec))

    #
    cntr = 1
    for i in range(m):
        if i > 0 and l[i][1] != l[i-1][1]:
            cntr = 1
        l[i][2] = str(cntr).zfill(6)
        cntr += 1

    #
    l.sort(key=lambda x: x[0])
    for xx in l:
        print(xx[1],end="")
        print(xx[2])


if __name__ == '__main__':
    main()
