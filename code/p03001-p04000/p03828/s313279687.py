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
from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
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
    
    import math
    class Eratos:
        def __init__(self, num):
            '''
            O(nlglgn) で num までの素数判定テーブルを作る
            >>> e = Eratos(10)
            >>> e.table
            [False, False, True, True, False, True, False, True, False, False, False]
            '''
            assert(num >= 1)
            self.table_max = num
            # self.table[i] は i が素数かどうかを示す (bool)
            self.table = [False if i == 0 or i == 1 else True for i in range(num+1)]
            for i in range(2, int(math.sqrt(num)) + 1):
                if self.table[i]:
                    for j in range(i ** 2, num + 1, i):    # i**2 からスタートすることで定数倍高速化できる
                        self.table[j] = False
        
        def is_prime(self, num):
            '''
            O(1) で素数判定を行う
            >>> e = Eratos(100)
            >>> [i for i in range(1, 101) if e.is_prime(i)]
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            '''
            assert(num >= 1)
            if num > self.table_max:
                raise ValueError('Eratos.is_prime(): exceed table_max({}). got {}'.format(self.table_max, num))
            return self.table[num]
        
        def prime_factorize(self, num):
            '''
            O(√n) で素因数分解を行う
            >>> e = Eratos(10000)
            >>> e.prime_factorize(6552)
            {2: 3, 3: 2, 7: 1, 13: 1}
            '''
            assert(num >= 1)
            if int(math.sqrt(num)) > self.table_max:
                raise ValueError('Eratos.prime_factorize(): exceed prime table size. got {}'.format(num))
            # 素因数分解の結果を記録する辞書        
            factorized_dict = dict()
            candidate_prime_numbers = [i for i in range(2, int(math.sqrt(num)) + 1) if self.is_prime(i)]
            # n について、√n 以下の素数で割り続けると最後には 1 or 素数となる
            # 背理法を考えれば自明 (残された数が √n より上の素数の積であると仮定。これは自明に n を超えるため矛盾)
            for p in candidate_prime_numbers:
                if num == 1:    # これ以上調査は無意味
                    break
                if num % p == 0:
                    cnt = 0
                    while num % p == 0:
                        num //= p
                        cnt += 1
                    factorized_dict[p] = cnt
            if num != 1:
                factorized_dict[num] = 1
            return factorized_dict
        
        def enum_divisor(self, num):
            '''
            O(√n) で約数列挙を行う
            >>> e = Eratos(10000)
            >>> e.enum_divisor(4)
            [1, 2, 4]
            >>> e.enum_divisor(19)
            [1, 19]
            >>> e.enum_divisor(100)
            [1, 2, 4, 5, 10, 20, 25, 50, 100]
            '''
            divisor_small = []
            divisor_large = []
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisor_small.append(i)
                    if i != num // i:
                        divisor_large.append(num // i)
            divisor_large.reverse()
            return divisor_small + divisor_large
    
    n = ii()
    eratos = Eratos(n)
    if n == 1:
        print(1)
    else:
        c = Counter()
        for i in range(2, n+1):
            d = eratos.prime_factorize(i)
            c += Counter(d)
        ans = 1
        for k, v in c.items():
            ans = (ans * (v + 1)) % mod
        print(ans)


if __name__ == "__main__":
    main()
