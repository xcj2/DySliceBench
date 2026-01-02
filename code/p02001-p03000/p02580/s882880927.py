#!/usr/bin/env python3

import sys
from typing import Any, Callable, Deque, Dict, List, Mapping, Optional, Sequence, Set, Tuple, TypeVar, Union
# import time
# import math, cmath
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
# from heapq import _heapify_max, _heappop_max, _siftdown_max
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from fractions import Fraction               # Fraction(a, b) => a / b ∈ Q. note: Fraction(0.1) do not returns Fraciton(1, 10). Fraction('0.1') returns Fraction(1, 10)



def main():
    Num = Union[int, float]
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79e+308
    # inf = 2 ** 63 - 1             # (for fast JIT compile in PyPy) 9.22e+18
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input():  return sys.stdin.readline().rstrip()
    def ii():     return int(input())
    def isp():    return input().split()
    def mi():     return map(int, input().split())
    def mi_0():   return map(lambda x: int(x)-1, input().split())
    def lmi():    return list(map(int, input().split()))
    def lmi_0():  return list(map(lambda x: int(x)-1, input().split()))
    def li():     return list(input())
    def debug(x): print(x, file=sys.stderr)
    # def _heappush_max(h, item): h.append(item); _siftdown_max(h, 0, len(h)-1)
    
    
    h, w, m = mi()
    bombs = [tuple(mi_0()) for _ in range(m)]
    bombs_set = set(bombs)

    x_count = [0] * h
    y_count = [0] * w
    for x, y in bombs:
        x_count[x] += 1
        y_count[y] += 1
    
    hm = max(x_count)
    wm = max(y_count)
    hm_group = [i for i, elm in enumerate(x_count) if elm == hm]
    wm_group = [i for i, elm in enumerate(y_count) if elm == wm]
    
    def check_no_bomb():
        # hm とする x, wm とする w のうち好きな組み合わせで bomb がない座標を引き当てられるか？
        if len(hm_group) * len(wm_group) > m:
            # 直積のどれかしらは bomb ではない
            return True
        else:
            # 直積を調べられる
            for x in hm_group:
                for y in wm_group:
                    if (x, y) not in bombs_set:
                        return True
            return False    
    
    print(hm + wm if check_no_bomb() else hm + wm - 1)






if __name__ == "__main__":
    main()
