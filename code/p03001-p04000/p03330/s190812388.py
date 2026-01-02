#!/usr/bin/env python3

import sys
# import time
# import math
# import numpy as np
# import scipy.sparse.csgraph as cs            # csgraph_from_dense(ndarray, null_value=inf), bellman_ford(G, return_predecessors=True), dijkstra, floyd_warshall
# import random                                # random, uniform, randint, randrange, shuffle, sample
# import string                                # ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from datetime import date, datetime          # date.today(), date(year,month,day) => date obj; datetime.now(), datetime(year,month,day,hour,second,microsecond) => datetime obj; subtraction => timedelta obj
# from datetime.datetime import strptime       # strptime('2019/01/01 10:05:20', '%Y/%m/%d/ %H:%M:%S') returns datetime obj
# from datetime import timedelta               # td.days, td.seconds, td.microseconds, td.total_seconds(). abs function is also available.
# from copy import copy, deepcopy              # use deepcopy to copy multi-dimentional matrix without reference
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict (e.g. list is not allowed)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from fractions import gcd                    # for Python 3.4 (previous contest @AtCoder)



def main():
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79...e+308
    # inf = 2 ** 64 - 1             # (for fast JIT compile in PyPy) 1.84...e+19
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())

    
    n, c = mi()
    color_cost = [lmi() for _ in range(c)]    # color x -> color y (0 to c-1 表現) にかかる擦ろtは color_cost[x][y]

    # color_cost = np.zeros((c, c), dtype="int16")
    # for i in range(c):
    #     tmp = lmi()
    #     for j in range(c):
    #         color_cost[i, j] = tmp[j]


    group = [[] for _ in range(3)]    # 0-index で i+j%3=0, 1, 2 となるやつら
    for i in range(n):
        tmp = lmi_0()    # color を 0 to c-1 表現に
        # print(tmp)
        for j in range(n):
            group[(i+j)%3].append(tmp[j])
    
    zero, one, two = group
    # O(n^2) で前処理
    zero_cnt, one_cnt, two_cnt = map(lambda x: Counter(x), group)

    ans = 10**15
    # O(30*29*28) (= O(2*10^4)) * O(C)
    for color_zero, color_one, color_two in permutations(range(c), r=3):
        cost = 0
        for col, v in zero_cnt.items():
            cost += v * color_cost[col][color_zero]
        for col, v in one_cnt.items():
            cost += v * color_cost[col][color_one]
        for col, v in two_cnt.items():
            cost += v * color_cost[col][color_two]
        ans = min(ans, cost)
    print(ans)



if __name__ == "__main__":
    main()

"""
O(10^7) だけど通らないっぽい <- 勘違い O(30*29*28* n) ではなく O(30*29*28* n * n) なので O(6*10^9)
辞書化の前処理で O(30*29*28 * c) = O(10**5) に
"""