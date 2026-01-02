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
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import combinations, combinations_with_replacement
from itertools import accumulate             # accumulate(iter[, f])
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from fractions import Fraction               # Fraction(a, b) => a / b ∈ Q. note: Fraction(0.1) do not returns Fraciton(1, 10). Fraction('0.1') returns Fraction(1, 10)
# from fractions import gcd                    # for Python 3.4 (previous contest @AtCoder)



def main():
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79e+308
    # inf = 2 ** 63 - 1             # (for fast JIT compile in PyPy) 9.22e+18
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def isp():   return input().split()
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())

    def convert_to_alpha(num):
        return chr(ord('a') + num - 1)    # num は 1 - 25
    
    n = ii()
    memo = [pow(26, i+1) for i in range(20)]
    accum = list(accumulate(memo))
    least = list(accumulate([pow(26, i) for i in range(20)]))
    digit = 0
    for i in range(20):
        if accum[i] >= n:
            digit = i
            break
    L = []
    # [0], ..., [digit] までアルファベットが入る
    for i in range(digit, -1, -1):
        # print(f"{L} {n} {i}")
        if i == 0:
            assert 1 <= n <= 26
            if n == 26:
                L.append('z')
            else:
                L.append(convert_to_alpha(n))
            break
        # pow(26, i) to pow(26, i+1) だけど
        assert accum[i-1] <= n <= accum[i]
        if n >= pow(26, i+1) + least[i-1]:
            L.append('z')
            n -= pow(26, i+1)
        else:
            q = (n - least[i-1]) // pow(26, i)
            res = n - q * pow(26, i)
            if res < least[i-1]:
                q -= 1
            if q == 26:
                L.append('z')
            else:
                L.append(convert_to_alpha(q))
            n = res
        


    print(''.join(L))


if __name__ == "__main__":
    main()
