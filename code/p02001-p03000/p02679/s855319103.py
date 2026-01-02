#!/usr/bin/env python3

import sys
# import time
from math import gcd
# import numpy as np
# import scipy.sparse.csgraph as cs            # csgraph_from_dense(ndarray, null_value=inf), bellman_ford(G, return_predecessors=True), dijkstra, floyd_warshall
# import random                                # random, uniform, randint, randrange, shuffle, sample
# import string                                # ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
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
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
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


    def standardization(a, b):
        """
        (a, b) で表される方向ベクトルをシンプルな整数ペアの方向ベクトルへ変換する
        処理後は第一、第四象限に方向ベクトルが集中する
        """
        assert (a != 0 or b != 0)
        if a == 0:
            return (0, 1)
        if b == 0:
            return (1, 0)
        g = gcd(a, b)
        a //= g
        b //= g
        # 第一項は正になるように
        # 原点対照にしてもベクトルの直行性は変わらない
        return (a, b) if a > 0 else (-a, -b)

    
    n = ii()
    L = [lmi() for _ in range(n)]

    dict_b_pos = defaultdict(int)
    dict_b_neg = defaultdict(int)
    origin = 0
    for a, b in L:
        if a == 0 and b == 0:
            origin += 1
            continue
        a, b = standardization(a, b)
        if b <= 0:
            dict_b_neg[(a, b)] += 1
        else:
            dict_b_pos[(b, -a)] += 1    # 対応するものはこれ
            dict_b_neg[(b, -a)] += 0    # 対応するスロットだけ作っておきループが回るようにする
    
    # print(dict_b_neg)
    # print(dict_b_pos)
    ans = origin
    tmp = 1
    for key, u in dict_b_neg.items():
        v = dict_b_pos[key]
        tmp = (tmp * (1 + pow(2, u, mod) - 1 + pow(2, v, mod) - 1)) % mod
    ans += tmp
    ans -= 1    # 全部使わないパターンを除く

    print(ans % mod)


if __name__ == "__main__":
    main()
