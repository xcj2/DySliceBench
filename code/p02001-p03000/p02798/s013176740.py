#!/usr/bin/env python3

import sys
from typing import Any, Callable, Deque, Dict, List, Mapping, Optional, Sequence, Set, Tuple, TypeVar, Union
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
from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from fractions import Fraction               # Fraction(a, b) => a / b ∈ Q. note: Fraction(0.1) do not returns Fraciton(1, 10). Fraction('0.1') returns Fraction(1, 10)



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
    

    def check_increasing(L):
        for i in range(1, n):
            if L[i][0] < L[i-1][0]:
                return False
        return True


    def modified_merge(left, right):
        '''
        ソート済み配列 left, right を受け取り、 O(n) で全体のソート済み配列を生成する
        マージの過程で転倒数をメモして返す

        >>> modified_merge([1, 5, 7], [2, 3, 3])
        (6, [1, 2, 3, 3, 5, 7])

        Args:
            left (list)
            right (list)
        Returns:
            inv (int)
            sorted_list (list)
        '''
        sorted_list = []
        i, j, inv = 0, 0, 0
        buf_1 = left[:] + [float('inf')]
        buf_2 = right[:] + [float('inf')]
        for _ in range(len(left) + len(right)):
            if buf_1[i] < buf_2[j]:
                sorted_list.append(buf_1[i])
                i += 1
                inv += j
            else:
                sorted_list.append(buf_2[j])
                j += 1
        return inv, sorted_list


    def modified_merge_sort(L, i, j):
        '''
        [i, j), つまりL[i:j] を O(nlgn) で非破壊的かつ安定にマージソートする
        マージソートの過程で転倒数をメモして返す
        
        >>> modified_merge_sort([3, 5, 2, 1, 0], 0, 5)
        (9, [0, 1, 2, 3, 5])

        Args:
            L (list)
            i (int)
            j (int)
        Returns:
            inv (int)
            sorted_list (list)
        '''
        if i + 1 == j:
            # L[i:j+1] = [L[i]]
            return 0, [L[i]]
        mid = (i + j) // 2
        left_inv_cnt, left = modified_merge_sort(L, i, mid)
        right_inv_cnt, right = modified_merge_sort(L, mid, j)
        merge_inv_cnt, sorted_list = modified_merge(left, right)
        return left_inv_cnt + right_inv_cnt + merge_inv_cnt, sorted_list


    def count_inversion(L):
        '''
        O(nlgn) で L の要素の転倒数を求める

        >>> count_inversion([1, 9, 2, 7, 5, 6, 4, 8, 3, 0])
        26
        '''
        cnt, _ = modified_merge_sort(L, 0, len(L))
        return cnt


    def calc_swapflip(L):
        return count_inversion(list(map(lambda x: x[1], L)))

    
    n = ii()
    A = lmi()
    B = lmi()

    ans = inf

    w = [(A[i], i, B[i]) if i % 2 == 0 else (B[i], i, A[i]) for i in range(n)]
    # w.sort(key=itemgetter(0))
    w.sort()

    for pattern in combinations(w, r=(n+1)//2):
        # print(pattern)
        left = [(elm[2], elm[1], elm[0]) for elm in w if elm not in pattern]
        # left.sort(key=itemgetter(0))
        left.sort()
        concat = []
        for i in range(n//2):
            concat.append(pattern[i])
            concat.append(left[i])
        if n % 2 == 1:
            concat.append(pattern[-1])

        if check_increasing(concat):
            op = calc_swapflip(concat)
            # print(concat)            
            # print(op)
            ans = min(ans, op)

    print(ans) if ans != inf else print(-1)
        




if __name__ == "__main__":
    main()
