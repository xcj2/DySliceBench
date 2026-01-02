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

# from fractions import gcd
# from math import gcd

# def lcm(n, m):
#     return int(n * m / gcd(n, m))


# def coprimize(p, q):
#     common = gcd(p, q)
#     return (p // common, q // common)


# def find_gcd(list_l):
#     x = reduce(gcd, list_l)
#     return x


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def main():
    n, m, x = map(int, input().strip().split())
    books = []
    for i in range(n):
        c_temp, *A_temp = map(int, input().strip().split())
        books.append((c_temp, A_temp))
    eprint('books ', end=':\n')
    eprint(books)

    #
    ans = sys.maxsize
    for case in range(2 ** n):	 # 場合ループ # nは人とかモノとかの個数
        l_bin = list(map(int, (format(case, 'b').zfill(n))))
        # eprint('l_bin ',end=': ')
        # eprint(l_bin)

        # flag=0
        lvalue = [0 for _ in range(m)]
        cost = 0
        for index_object in range(n):	  # 人とかモノとかループ
            if l_bin[index_object] == 1:				   # その桁がyesだと仮定している場合
                cost += books[index_object][0]
                for j in range(m):
                    lvalue[j] += books[index_object][1][j]
                    
            else:								 # その桁がnoだと仮定している場合
                pass
        #
        suc_flag = 1
        for i in range(m):
            suc_flag *= (lvalue[i] >= x)
        if suc_flag:
            ans = min(ans, cost)
    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
