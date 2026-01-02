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


    def make_top_constraints(n, L):
        top_c = [tuple() for _ in range(n+1)]
        top_c[0] = (1, 1)    # 確定
        for i in range(1, n+1):
            # 上が取りうる最小ノードで、そこから葉を除いたノードたちから 1 本しか伸びていないケース
            minimum = max(top_c[i-1][0] - L[i-1], 0)    # さすがに 0 以上
            # 上が取りうる最大ノードで、そこから葉を除いたノードたちから 2 本ずつ伸びているケース
            maximum = max((top_c[i-1][1] - L[i-1]) * 2, 0)
            top_c[i] = (minimum, maximum)
        return top_c


    def make_bottom_constraints(n, L):
        bottom_c = [tuple() for _ in range(n+1)]
        bottom_c[n] = (L[n], L[n])    # 確定
        for i in range(n-1, -1, -1):
            # 下が取りうる最小ノードで、そこから 2 本合流 + この深さの葉
            minimum = bottom_c[i+1][0] // 2 + L[i]
            # 下が取りうる最大ノードで、そこから 1 本ずつ親に向かって伸びる + この深さの葉
            maximum = bottom_c[i+1][1] + L[i]
            bottom_c[i] = (minimum, maximum)
        return bottom_c


    def max_cross_num(L1, L2):
        left = max(L1[0], L2[0])
        right = min(L1[1], L2[1])
        if left > right:
            return -1
        else:
            return right


    def calc_max_node(n, top_down_constraints, bottom_up_constraints):
        cnt = 0
        for i in range(n+1):
            num = max_cross_num(top_down_constraints[i], bottom_up_constraints[i])
            # print(f"i:{i} node_num:{num}")
            if num < 0:
                return -1
            cnt += num
        return cnt
    
    
    n = ii()
    L = lmi()

    # constraints from d=0
    top_down_constraints = make_top_constraints(n, L)
    # constraints from d=n
    bottom_up_constraints = make_bottom_constraints(n, L)

    # print(top_down_constraints)
    # print(bottom_up_constraints)

    print(calc_max_node(n, top_down_constraints, bottom_up_constraints))


if __name__ == "__main__":
    main()
