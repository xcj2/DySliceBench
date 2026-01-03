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
from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
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
    
    
    class PQueueMin:
        def __init__(self):
            self.pq = []    # 第一要素に cost、第二要素に ind が来る様にする
        
        def push(self, ind, cost):
            heappush(self.pq, [cost, ind])
        
        def pop(self):
            cost, ind = heappop(self.pq)
            return [ind, cost]
    
        def is_empty(self):
            return len(self.pq)==0
    
    
    
    def dijkstra(adj_with_weight, start):
        '''
        Dijkstra 法 O((E+V)lgV) (頂点を回るときに最小のものを取り出していくのに VlgV, cost の更新で ElgV)
        負辺を含まぬ重みつきグラフについて、ある頂点から他の頂点までの最短コストを貪欲に計算する
        '''
        V = len(adj_with_weight)
        cost = [float('inf')] * V
        previous = [None] * V
        cost[start] = 0
        fixed = [False] * V
        pq = PQueueMin()
        # 最初は始点が必ずコスト最小。pq に突っ込む
        pq.push(start, cost[start])
        while not pq.is_empty():
            # 現段階で最短のコストとなっている頂点を選択
            u, cost_of_u = pq.pop()
            fixed[u] = True
            for v, weight_of_uv in adj_with_weight[u]:
                if not fixed[v] and cost[v] > cost_of_u + weight_of_uv:
                    cost[v] = cost_of_u + weight_of_uv
                    previous[v] = u
                    pq.push(v, cost[v])
        return cost, previous
    
    n, m = mi()
    adj_with_weight = [[] for _ in range(n)]
    edge_matrix = [[False] * n for _ in range(n)]    # あとで最短経路として使ったかどうかのメモ
    for _ in range(m):
        a, b, c = mi()
        a -= 1
        b -= 1
        adj_with_weight[a].append((b, c))
        adj_with_weight[b].append((a, c))
    
    for i in range(n):
        _, previous = dijkstra(adj_with_weight, i)
        # print(previous)
        for j in range(n):
            if j != i:
                u = previous[j]
                j, u = min(j, u), max(j, u)
                edge_matrix[j][u] = True
    # print(edge_matrix)
    
    cnt = 0
    for u in range(n):
        for v, _ in adj_with_weight[u]:
            if u < v and not edge_matrix[u][v]:
                cnt += 1
    print(cnt)
    

    



if __name__ == "__main__":
    main()
