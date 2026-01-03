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
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from datetime import date, datetime          # date.today(), date(year,month,day) => date obj; datetime.now(), datetime(year,month,day,hour,second,microsecond) => datetime obj; subtraction => timedelta obj
# from datetime.datetime import strptime       # strptime('2019/01/01 10:05:20', '%Y/%m/%d/ %H:%M:%S') returns datetime obj
# from datetime import timedelta               # td.days, td.seconds, td.microseconds, td.total_seconds(). abs function is also available.
# from copy import copy, deepcopy              # use deepcopy to copy multi-dimentional matrix without reference
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict (e.g. list is not allowed)
from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
from operator import itemgetter              # itemgetter(1), itemgetter('key')
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
    
    
    n = ii()
    L = lmi()
    
    left = sum(L[:n])
    l_h = L[:n]    # 現在前半 n 要素で使っているやつらが入った min heap
    heapify(l_h)

    right = 0
    tmp = [[i, L[i]] for i in range(n, 3*n)]
    assert (len(tmp) == 2*n)
    tmp.sort(key=itemgetter(1))
    latter_min_nth = [False] * 3 * n    # 0...n-1 は意味なし, 後半 n 要素で使っている奴らがメモられたリスト
    sub_member_r_h = []    # 現在後半 n 要素の控えメンバーたちが入った min heap
    for ind in range(n):
        i, num = tmp[ind]
        right += num
        latter_min_nth[i] = True
    for ind in range(n, 2*n):
        i, num = tmp[ind]
        sub_member_r_h.append([num, i])
    heapify(sub_member_r_h)        
    

    max_score = left - right
    # print(max_score)
    for i in range(n, 2*n):
        # L[i] を前半で使える側へと移動する
        if l_h[0] < L[i]:
            # これを使った方が大きくできる
            left -= heappop(l_h)
            left += L[i]
            heappush(l_h, L[i])
        if latter_min_nth[i]:
            # 後半 n 要素で使われているものが失われた
            latter_min_nth[i] = False
            right -= L[i]
            while sub_member_r_h[0][1] <= i:
                heappop(sub_member_r_h)    # すでに使えないものは捨てる
            num, ind = heappop(sub_member_r_h)
            assert (ind > i)
            right += num
            latter_min_nth[ind] = True
        # print(f"{i} {left} {right}")
        max_score = max(max_score, left - right)
    
    print(max_score)


if __name__ == "__main__":
    main()



"""
15 
25 sub
"""