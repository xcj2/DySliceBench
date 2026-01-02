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
# from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from fractions import Fraction               # Fraction(a, b) => a / b ∈ Q. note: Fraction(0.1) do not returns Fraciton(1, 10). Fraction('0.1') returns Fraction(1, 10)



def main():
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def isp():   return input().split()
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())


    def enum_divisor(num):
        i = 1
        left = []
        right = []
        while i ** 2 < num:
            if num % i == 0:
                left.append(i)
                right.append(num // i)
            i += 1
        if i ** 2 == num:
            return left + [i] + list(reversed(right))
        else:
            return left + list(reversed(right))
    

    def is_ok(m, k, L):
        mod_list = [elm % m for elm in L]
        plus_group, minus_group = [], []
        plus_cnt, minus_cnt = 0, 0
        for mod_num in mod_list:
            if mod_num <= m - mod_num:
                minus_group.append(mod_num)
                minus_cnt += mod_num
            else:
                plus_group.append(mod_num)
                plus_cnt += m - mod_num
        
        # print(f"m {m} plus {plus_group} minus {minus_group}")
        # print(f"pluscnt {plus_cnt} minuscnt {minus_cnt}")
        assert abs(plus_cnt - minus_cnt) % m == 0
        cnt = plus_cnt + minus_cnt
        if plus_cnt > minus_cnt:
            # plus のグループを minus のグループに転じる必要がある
            plus_group.sort()
            for i in range((plus_cnt - minus_cnt) // m):
                mod_num = plus_group[i]
                cnt += (mod_num - (m - mod_num))
        else:
            # minus のグループを plus のグループに
            minus_group.sort(reverse=True)
            for i in range((minus_cnt - plus_cnt) // m):
                mod_num = minus_group[i]
                cnt += ((m - mod_num) - mod_num)
        # print(f"cnt {cnt}")
        assert cnt % 2 == 0
        return cnt // 2 <= k
    

    n, k = mi()
    L = lmi()
    s = sum(L)
    div = enum_divisor(s)
    div.reverse()


    for m in div:
        if is_ok(m, k, L):
            print(m)
            break







if __name__ == "__main__":
    main()
