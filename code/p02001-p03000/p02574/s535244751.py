#!/usr/bin/env python3

import sys
from typing import Any, Callable, Deque, Dict, List, Mapping, Optional, Sequence, Set, Tuple, TypeVar, Union
# import time
# import math, cmath
from math import gcd
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
        
    class Eratos:
        def __init__(self, num: int):
            '''
            O(nlglgn) で num までの素数判定テーブルを作る
            >>> e = Eratos(10)
            >>> e.table
            [False, False, True, True, False, True, False, True, False, False, False]
            '''
            if num < 1:
                raise ValueError(f'Eratos.__init__(): argument should be >= 1. got {num}')
            self.table_max = num
            # self.table[i] は i が素数かどうかを示す (bool)
            self.table = [False if i == 0 or i == 1 else True for i in range(num+1)]
            i = 2
            while i ** 2 <= num:
                if self.table[i]:
                    for j in range(i ** 2, num + 1, i):    # i**2 からスタートすることで定数倍高速化できる
                        self.table[j] = False
                i += 1   


        def is_prime(self, num: int) -> bool:
            '''
            O(1) で素数判定を行う
            >>> e = Eratos(100)
            >>> [i for i in range(1, 101) if e.is_prime(i)]
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            '''
            if num < 1:
                raise ValueError(f'Eratos.is_prime(): argument shoule be >= 1. got {num}')
            if num > self.table_max:
                raise ValueError(f'Eratos.is_prime(): exceed table_max({self.table_max}). got {num}')
            return self.table[num]

        # def prime_factorize(self, num: int) -> Dict[int, int]:
        #     '''
        #     O(√n) で素因数分解を行う
        #     >>> e = Eratos(10000)
        #     >>> e.prime_factorize(6552)
        #     {2: 3, 3: 2, 7: 1, 13: 1}
        #     '''
        #     if num < 1:
        #         raise ValueError(f'Eratos.prime_factorize(): argument shoule be >= 1. got {num}')
        #     if (self.table_max + 1) ** 2 < num:
        #         raise ValueError('Eratos.prime_factorize(): exceed prime table size. got {}'.format(num))
        #     # 素因数分解の結果を記録する辞書        
        #     factorized_dict = dict()
        #     # n について、√n 以下の素数で割り続けると最後には 1 or 素数となる
        #     # 背理法を考えれば自明 (残された数が √n より上の素数の積であると仮定。これは自明に n を超えるため矛盾)
        #     for p in self.candidate:
        #         if num == 1:    # これ以上調査は無意味
        #             break
        #         if num % p == 0:
        #             # cnt = 0
        #             while num % p == 0:
        #                 num //= p
        #                 # cnt += 1
        #             # factorized_dict[p] = cnt
        #             factorized_dict[p] = 1
        #     if num != 1:
        #         factorized_dict[num] = 1
        #     return factorized_dict


    def check_setwise(n, L):
        gcd_memo = L[0]        
        for i in range(n):
            gcd_memo = gcd(L[i], gcd_memo)
        return gcd_memo == 1


    def check_pairwise(n, L):
        eratos = Eratos(10**3+1)
        # 2 to 10 ** 3 (168 個)
        p_list = [p for p in range(2, 10**3+1) if eratos.is_prime(p)]
        # print(p_list)
        divided = [0] * n
        memo = set()
        for i in range(n):
            num = L[i]
            for p in p_list:
                if num == 1:
                    break
                if num % p == 0:
                    while num % p == 0:
                        num //= p
                    if p in memo:
                        return False
                    else:
                        memo.add(p)
            divided[i] = num
        # print(divided)
        rem_one = [elm for elm in divided if elm != 1]
        return len(rem_one) == len(set(rem_one))


    n = ii()
    L = lmi()
    if check_pairwise(n, L):
        print('pairwise coprime')
    elif check_setwise(n, L):
        print('setwise coprime')
    else:
        print('not coprime')


if __name__ == "__main__":
    main()
