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
    
    def make_factorial_table(size, mod):
        fact_mod = [1] * (size + 1)
        for i in range(1, size + 1):
            fact_mod[i] = (fact_mod[i - 1] * i) % mod
        return fact_mod


    def make_inv_factorial_table(size: int, mod: int) -> List[int]:
        inv_fact_mod = [1] * (size + 1)
        n_fact = 1
        for i in range(2, size+1):
            n_fact = (n_fact * i) % mod
        inv_fact_mod[size] = pow(n_fact, mod-2, mod)    # a ^ p-2 ≡ 1/a (mod p) において a = n! とする。 1/n! (mod p) を求める
        for i in range(size-1, -1, -1):
            inv_fact_mod[i] = (inv_fact_mod[i+1] * (i+1)) % mod    # 1/(n-1)! = 1/n! * n
        return inv_fact_mod    


    def combination(n: int, r: int, mod: int, fact_table: List[int], inv_fact_table: List[int]=[]) -> int:
        numerator = fact_table[n]
        if not inv_fact_table:
            # pow はすでに繰り返し二乗法で効率的に実装されている
            denominator = pow((fact_table[n-r] * fact_table[r]) % mod, mod-2, mod)
        else:
            denominator = (inv_fact_table[n-r] * inv_fact_table[r]) % mod
            assert (fact_table[n-r] * inv_fact_table[n-r]) % mod == 1
            assert (fact_table[n-r] * fact_table[r] * inv_fact_table[n-r] * inv_fact_table[r]) % mod == 1
            assert pow((fact_table[n-r] * fact_table[r]) % mod, mod-2, mod) == denominator
        return (numerator * denominator) % mod



    n, m = mi()
    f = make_factorial_table(10 ** 6, mod)
    inv = make_inv_factorial_table(10 ** 6, mod)

    # Σ {k=0 to n} (nCk * (-1)^k * mPk * (m-kPn-k)^2)
    ans = 0
    for k in range(n + 1):
        if k % 2 == 0:
            cnt = 1
        else:
            cnt = -1
        cnt = (cnt * combination(n, k, mod, f, inv)) % mod
        cnt = (cnt * (combination(m, k, mod, f, inv) * f[k]) % mod) % mod
        cnt = (cnt * (combination(m-k, n-k, mod, f, inv) * f[n-k] % mod) ** 2 % mod) % mod
        ans = (ans + cnt) % mod
    print(ans)



if __name__ == "__main__":
    main()

