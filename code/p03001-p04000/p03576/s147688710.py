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
    
    

    # class TwoDimNode:
    #     def __init__(self, x=None, y=None, parent=None, left=None, right=None):
    #         '''
    #         2 次元二分探索木のためのノード
    #         '''        
    #         self.x = x
    #         self.y = y
    #         self.parent = parent
    #         self.left = left
    #         self.right = right
    #         self.flag = True
    
    # class TwoDimTree:
    #     def __init__(self, points=[]):
    #         '''
    #         2 次元二分探索木 (kD tree) を作成する
    #         root の深さを 0 として、深さが偶数の場合そこでは x を基準に、奇数の場合 y を基準に二分探索木条件を満たすようにする
    #         '''
    #         # nil の設定
    #         self.nil = TwoDimNode()
    #         self.nil.parent = self.nil
    #         self.nil.left = self.nil
    #         self.nil.right = self.nil
    #         # root の設定
    #         self.root = self.nil
    #         # もし予め一次元の点の集合が与えられるのならバランスする形で kD tree を構築する
    #         self._balance_insert(points)
        
    #     # def preorder_traverse(self, node=None):
    #     #     node = self.root if node is None else node
    #     #     if node != self.nil:
    #     #         print(f'({node.x},{node.y})', end=' ')
    #     #         self.preorder_traverse(node=node.left)
    #     #         self.preorder_traverse(node=node.right)
            
    #     # def postorder_traverse(self, node=None):
    #     #     node = self.root if node is None else node
    #     #     if node != self.nil:
    #     #         self.preorder_traverse(node=node.left)
    #     #         self.preorder_traverse(node=node.right)
    #     #         print(f'({node.x},{node.y})', end=' ')
    
    #     # def inorder_traverse(self, node=None):
    #     #     node = self.root if node is None else node
    #     #     if node != self.nil:
    #     #         self.preorder_traverse(node=node.left)
    #     #         print(f'({node.x},{node.y})', end=' ')
    #     #         self.preorder_traverse(node=node.right)
        
    #     def _balance_insert(self, seq, depth=0):
    #         # 毎回 x or y をキーとしてソートを行い、中央値をとって insert すれば平衡になる
    #         if seq:
    #             arranged = sorted(seq, key=itemgetter(depth % 2))
    #             mid = len(seq) // 2
    #             self.insert(arranged[mid][0], arranged[mid][1])
    #             self._balance_insert(arranged[:mid], depth+1)
    #             self._balance_insert(arranged[mid+1:], depth+1)
    
    
    #     def insert(self, x, y):
    #         '''
    #         kD tree に値が (x, y) であるノードを O(depth) で挿入する
    #         (コンストラクタで生成した kD tree は平衡であることが保証されるが、insert により生成した部分の平衡性は保証されないことに注意)        
    #         '''
    #         trailer = self.nil    # (x, y) を挿入するべき nil の一つ前のノードを保存するトレーラポインタ
    #         pos = self.root    # (x, y) を挿入するべき nil の場所を探す
    #         depth = 0
    #         while pos != self.nil:
    #             trailer = pos
    #             k, pos_k = (x, pos.x) if depth % 2 == 0 else (y, pos.y)
    #             if k < pos_k:
    #                 pos = pos.left
    #             elif pos_k < k:
    #                 pos = pos.right
    #             else:
    #                 pos.flag ^= pos.flag
    #                 pos = pos.left if pos.flag else pos.right
    #             depth += 1
    #         inserted_node = TwoDimNode(x, y, trailer, self.nil, self.nil)
    #         # trailer の depth
    #         depth -= 1
    #         k, trailer_k = (x, trailer.x) if depth % 2 == 0 else (y, trailer.y)
    #         # tree is empty
    #         if trailer == self.nil:
    #             self.root = inserted_node
    #         # どこかのノードの子供の位置に挿入する時
    #         elif k < trailer_k or (k == trailer_k and trailer.flag):
    #             trailer.left = inserted_node
    #         else:
    #             trailer.right = inserted_node
        
    #     def two_dim_search(self, sx, tx, sy, ty, node=None, depth=0):
    #         '''
    #         kD tree に対し閉区間 D = {(x, y) | sx<=x<=tx, sy<=y<=ty} 内に存在する点を探してリストにまとめて返す (対応する点の個数 k として O(√n + k))
    #         下記のように検索必要性を判断し再帰的に左右の子に対し探索を行えば良い
    
    #         <-------- node.x -------->
    #         <----------->
    #         少しでも [sx,tx] が左側ゾーン ((-inf, node.x]) に被っていたら検索しておく必要がある
    #                     <----->
    #                     少しでも [sx, tx] が右側ゾーン ([node.x, inf)) に被っていたら検索しておく必要がある
    #         '''        
    #         # buf = []
    #         # node = self.root if node is None else node
    #         # # print(f'{node.x} {node.y}')
    #         # if depth % 2 == 0:
    #         #     if node.left != self.nil and sx <= node.x:
    #         #         buf += self.two_dim_search(sx, tx, sy, ty, node.left, depth+1)
    #         #     if sx <= node.x <= tx and sy <= node.y <= ty:
    #         #         buf.append((node.x, node.y))
    #         #     if node.right != self.nil and tx >= node.x:
    #         #         buf += self.two_dim_search(sx, tx, sy, ty, node.right, depth+1)
    #         # else:
    #         #     if node.left != self.nil and sy <= node.y:
    #         #         buf += self.two_dim_search(sx, tx, sy, ty, node.left, depth+1)
    #         #     if sx <= node.x <= tx and sy <= node.y <= ty:
    #         #         buf.append((node.x, node.y))
    #         #     if node.right != self.nil and ty >= node.y:
    #         #         buf += self.two_dim_search(sx, tx, sy, ty, node.right, depth+1)
    #         # return buf
    #         cnt = 0
    #         node = self.root if node is None else node
    #         if depth % 2 == 0:
    #             if node.left != self.nil and sx <= node.x:
    #                 cnt += self.two_dim_search(sx, tx, sy, ty, node.left, depth+1)
    #             if sx <= node.x <= tx and sy <= node.y <= ty:
    #                 cnt += 1
    #             if node.right != self.nil and tx >= node.x:
    #                 cnt += self.two_dim_search(sx, tx, sy, ty, node.right, depth+1)
    #         else:
    #             if node.left != self.nil and sy <= node.y:
    #                 cnt += self.two_dim_search(sx, tx, sy, ty, node.left, depth+1)
    #             if sx <= node.x <= tx and sy <= node.y <= ty:
    #                 cnt += 1
    #             if node.right != self.nil and ty >= node.y:
    #                 cnt += self.two_dim_search(sx, tx, sy, ty, node.right, depth+1)
    #         return cnt

    def count_inner_points(points, sx, tx, sy, ty):
        cnt = 0
        for x, y in points:
            if sx <= x <= tx and sy <= y <= ty:
                cnt += 1
        return cnt
    

    n, num_of_points = mi()
    points = [lmi() for _ in range(n)]
    x_sorted_p = sorted(points, key=itemgetter(0))
    y_sorted_p = sorted(points, key=itemgetter(1))
    # kd = TwoDimTree(points)

    area = inf
    for i in range(n-1):
        for j in range(i+1, n):
            sx, tx = x_sorted_p[i][0], x_sorted_p[j][0]
            # # 枝刈り、TLE ケースを 10 -> 3 にしてくれた
            # if kd.two_dim_search(sx, tx, y_sorted_p[0][1], y_sorted_p[-1][1]) < num_of_points:
            #     continue
            if count_inner_points(points, sx, tx, y_sorted_p[0][1], y_sorted_p[-1][1]) < num_of_points:
                continue
            for k in range(n-1):
                for l in range(k+1, n):
                    sy, ty = y_sorted_p[k][1], y_sorted_p[l][1]
                    # if kd.two_dim_search(sx, tx, sy, ty) >= num_of_points:
                    #     # print(f"{sx} {tx} {sy} {ty} {kd.two_dim_search(sx, tx, sy, ty)}")
                    #     area = min(area, abs(tx - sx) * abs(ty - sy))
                    cnt = count_inner_points(points, sx, tx, sy, ty)
                    # if cnt > num_of_points:
                    #     continue
                    if cnt == num_of_points:
                        area = min(area, abs(tx - sx) * abs(ty - sy))
    print(area)
    


if __name__ == "__main__":
    main()