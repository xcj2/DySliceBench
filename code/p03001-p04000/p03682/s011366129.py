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
from operator import itemgetter              # itemgetter(1), itemgetter('key')
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


    class UnionFindTree:
        def __init__(self, num_of_elm):
            '''
            0 ... num_of_elem - 1 まで数字で表される (0-index) グループを管理する union find tree を作成する (O(n))
            '''
            self.n = num_of_elm
            self.table = [i for i in range(self.n)]    # table[ind] は ind の親の index を表す。ind == table[ind] の時そのグループの root である。
            self.rank = [0] * self.n    # root となる ind について rank[ind] はその木の深さを表す。それ以外の ind については意味を持たない。
            self.group_size = [1] * self.n    # root となる ind について group_size[ind] はそのグループに属するメンバの個数を表す。それ以外の ind については意味を持たない。
        
        def _find_set(self, x):
            '''
            x の属するグループ番号を O(α(n)) で求める
            '''
            parent = self.table[x]
            if x == parent:
                return x
            else:
                root = self._find_set(parent)
                # 経路圧縮
                self.table[x] = root
                return root
        
        def is_same(self, x, y):
            '''
            x と y が同じグループに属するか O(α(n)) で判定する
            '''
            return self._find_set(x) == self._find_set(y)
    
        def union(self, x, y):
            '''
            x と y の属するグループを O(α(n)) で統合する
            '''
            shallow_root = self._find_set(x)
            deep_root = self._find_set(y)
            if self.rank[shallow_root] > self.rank[deep_root]:
                shallow_root, deep_root = deep_root, shallow_root
            # そもそも同一グループだった時
            if shallow_root == deep_root:
                return False
            # グループが異なるので union
            else:
                self.table[shallow_root] = deep_root
                self.group_size[deep_root] += self.group_size[shallow_root]
                # 深さが等しかったときはつけ加えられた側の rank をインクリメントする
                if self.rank[shallow_root] == self.rank[deep_root]:
                    self.rank[deep_root] += 1
                return True
    
        def akin_num(self, x):
            '''
            x の属するグループのサイズを O(1) で計算する
            '''
            x_root = self._find_set(x)
            return self.group_size[x_root]
    
        def print_group_id(self):
            print([self._find_set(x) for x in self.table])

    
    def kruskal(edges, n):
        uf = UnionFindTree(n)
        total_cost = 0
        edges.sort(key=itemgetter(2))
        for e in edges:
            u, v, weight = e
            if uf.union(u, v):
                total_cost += weight
        return total_cost


    n = ii()
    appeared = set()
    L = []
    cnt = 0
    for _ in range(n):
        x, y = mi()
        if (x, y) in appeared:    # 同じ座標の点はここで弾いておく
            n -= 1
            continue
        L.append([cnt, x, y])
        appeared.add((x, y))
        cnt += 1
    
    edges = []
    s = set()
    L.sort(key=itemgetter(1))    # x でソート
    for j in range(1, n):
        u, v = L[j][0], L[j-1][0]    # ind of points
        u, v = min(u, v), max(u, v)
        dist = min(abs(L[j][1] - L[j-1][1]), abs(L[j][2] - L[j-1][2]))
        s.add((u, v))
        edges.append((u, v, dist))
    L.sort(key=itemgetter(2))    # y でソート
    for j in range(1, n):
        u, v = L[j][0], L[j-1][0]    # ind of points
        u, v = min(u, v), max(u, v)
        # 重複はチェック
        if (u, v) not in s:
            dist = min(abs(L[j][1] - L[j-1][1]), abs(L[j][2] - L[j-1][2]))
            edges.append((u, v, dist))
    
    print(kruskal(edges, n))
    




if __name__ == "__main__":
    main()
