#!/usr/bin/env python3

import sys
# import time
# import math
# import numpy as np
# import scipy.sparse.csgraph as cs            # csgraph_from_dense(ndarray, null_value=inf), bellman_ford(G, return_predecessors=True), dijkstra, floyd_warshall
# import random                                # random, uniform, randint, randrange, shuffle, sample
# import string                                # ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
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
    
    
    # class MaxHeap:
    #     def __init__(self, seq):
    #         tmp = list(map(lambda x: -x, seq))
    #         heapify(tmp)
    #         self.h = tmp
    #     def push(self, num):
    #         heappush(self.h, - num)
    #     def pop(self):
    #         return -heappop(self.h)

    # n, a, b = mi()
    # hp = MaxHeap([ii() for _ in range(n)])
    # cnt = 0
    # while True:
    #     max_hp = hp.pop()
    #     if max_hp <= cnt * b:
    #         break
    #     else:
    #         hp.push(max_hp - (a - b))
    #         cnt += 1
    # print(cnt)

    def ceil_div_alternative(x, y):
        """
        Args:
            x, y (int)
        Returns:
            int
        
        ceil(x / y) を正確に返す (y を何整数倍すると x 以上になるか？の値)

        >>> ceil_div_alternative(4, 2)
        2
        >>> ceil_div_alternative(4, 3)
        2

        > ceil() 、 floor() 、および modf() 関数については、非常に大きな浮動小数点数が 全て 整数そのものになるということに注意してください。
        > 通常、Python の浮動小数点型は 53 ビット以上の精度をもたない (プラットフォームにおける C double 型と同じ) ので、
        > 結果的に abs(x) >= 2**52 であるような浮動小数点型 x は小数部分を持たなくなるのです。
        > 10 ** 15 + 0.2 == 10 ** 15
        > False
        > 10 ** 16 + 0.2 == 10 ** 16
        > True
        
        x / y が大きな浮動小数点数となる場合は ceil ではなく、この関数を使うようにする。
        """
        assert (isinstance(x, int) and isinstance(y, int))
        assert (x >= 0 and y > 0)
        return (x + y - 1) // y


    def can_defeat_predicate(hp_list, operation_times, a, b):
        n = len(hp_list)
        start = bisect_right(hp_list, b * operation_times)
        if start == n:
            return True
        else:
            res = [hp_list[i] - b * operation_times for i in range(start, n)]
            cnt = 0
            for elm in res:
                cnt += ceil_div_alternative(elm, a - b)
            return cnt <= operation_times


    def binary_search(hp_list, a, b):
        left = 0    # 絶対に倒せない操作回数
        right = 10**9+1    # 絶対に倒せる操作回数
        while right - left > 1:
            mid = (right + left) // 2
            if can_defeat_predicate(hp_list, mid, a, b):
                right = mid
            else:
                left = mid
        return right



    n, a, b = mi()
    hp = sorted([ii() for _ in range(n)])
    print(binary_search(hp, a, b))



if __name__ == "__main__":
    main()
