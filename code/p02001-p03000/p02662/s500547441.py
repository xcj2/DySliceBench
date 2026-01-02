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
    mod = 998244353                # 10^9+7
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


    # def my_update(seq, L):
    #     n = len(seq)
    #     for i in range(n-1):
    #         seq[i+1] += L[i]

    
    # n, s = mi()
    # L = lmi()
    # dp = [[0] * (n + 1) for j in range(s + 1)]    # chain の長さ、場合のかず
    # # print(dp)
    # for i in range(n):
    #     for j in range(s, -1, -1):
    #         if j == 0 and L[i] <= s:
    #             dp[L[i]][1] += 1
    #         elif j + L[i] <= s and dp[j]:
    #             my_update(dp[j + L[i]], dp[j])    # counter
    #     # print(dp)
    
    # ans = 0
    # for chain_len, num in enumerate(dp[s]):
    #     ans = (ans + pow(2, n - chain_len, mod) * num) % mod
    # print(ans)


    # write-up solution
    """
    Ai それぞれ選ぶ or 選ばないと選択して行った時、足して S にできる組み合わせは何パターンできるか？
    -> 
    まさに二項定理の発想
    fi = 1+x^Ai として
    T = {1, 2, 3} に対する答えは [x^S]f1*f2*f3
    T = {1, 2} に対する答えは [x^S]f1*f2 
    のように計算していく
    全パターン f1*f2*f3 + f1*f2 + f1*f3 + f2*f3 + f1 + f2 + f3 の [x^S] の値が答え
    
    ->
    (1+f1)*...*(1+fi)*...*(1+fn) の x^S の係数と一致
    [x^S] Π{i=1...n} (2 + x^Ai)
    を計算せよ、という問である
    """
    n, s = mi()
    A = lmi()
    power_memo = [0] * (s + 1)
    power_memo[0] = 2
    if A[0] <= s:
        power_memo[A[0]] = 1
    for i in range(1, n):
        # print(power_memo)
        for j in range(s, -1, -1):
            tmp = (power_memo[j] * 2) % mod
            if j - A[i] >= 0 and power_memo[j - A[i]]:
                tmp += power_memo[j - A[i]]
            power_memo[j] = tmp % mod
    # print(power_memo)
    print(power_memo[s])



if __name__ == "__main__":
    main()
