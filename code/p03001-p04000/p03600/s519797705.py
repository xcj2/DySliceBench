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
from copy import copy, deepcopy              # use deepcopy to copy multi-dimentional matrix without reference
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


    def warshall_floyd(adj_mat_with_weight):
        '''
        Warshall-Floyd 法 (O(V^3), 1 sec だと v~500 とかが限界)
        全点対間の最短経路を三次元 DP で求める
            - 定式化
            - dp[k+1][i][j] を 0...k, i, j なる頂点を使用できる時の i~j 最短距離とする (k+1=0 の時は e(i,j))
            - dp[k+1][i][j] = min(dp[k][i][j], dp[k][i][k+1]+dp[k][k+1][j])
            - 最後に必要なのは dp[V][i][j] 。上の漸化式をみるに 2 次元 array があれば使いまわしてメモリ節約できる。
        Args:
            adj_mat_with_weight (list): 重みを記録した隣接行列 (非接続頂点は inf)
        Returns:
            dp (list): dp[i][j] を見れば全頂点を使用可能な時の i j 最短距離がわかる。最後に dp[i][i] が負になっていたら負サイクルが存在するということ
        '''
        V = len(adj_mat_with_weight)
        # テーブル初期化
        dp = deepcopy(adj_mat_with_weight)
        for i in range(V):
            dp[i][i] = 0
        # 漸化式を解く
        for k in range(1, V+1):
            for i in range(V):
                for j in range(V):
                    # new 2d-table # old 2d-table
                    dp[i][j] = min(dp[i][j], dp[i][k-1]+dp[k-1][j])
        return dp

    def check_possible_structure(dp, adj_mat):
        n = len(adj_mat)
        for i in range(n):
            for j in range(i+1, n):
                if dp[i][j] < adj_mat[i][j]:
                    return False
        return True

    def calc_minimum_street(dp, adj_mat):
        n = len(adj_mat)
        total_dist = 0
        for i in range(n):
            for j in range(i+1, n):
                total_dist += adj_mat[i][j]
        # 削除していく
        for i in range(n):
            for j in range(i+1, n):
                # (i, j) の距離について
                dist = adj_mat[i][j]
                for k in range(n):
                    if k != i and k != j and dp[i][k] + dp[k][j] == dist:
                        total_dist -= dist
                        break
        return total_dist
    
    
    n = ii()
    adj_mat = [lmi() for _ in range(n)]
    dp = warshall_floyd(adj_mat)

    if not check_possible_structure(dp, adj_mat):
        print(-1)
    else:
        print(calc_minimum_street(dp, adj_mat))


if __name__ == "__main__":
    main()
