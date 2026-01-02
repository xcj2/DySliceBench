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
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
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


    class Edge:
        def __init__(self, here, to, weight, rev_edge):
            self.here = here
            self.to = to
            self.weight = weight
            self.rev_edge = rev_edge    # 逆辺への参照


    def bipartite_max_matching(adj_list):
        """
        偶数ノードと奇数ノードで二部グラフが構成されているとする
        偶数ノードから奇数ノードへ向かう辺を集めた隣接リストが渡されるので、超入口と出口を追加し、辺を接続し、逆辺も Edge クラスで張った形の隣接リストを作成。
        最大流を求めて最大マッチングを計算する
        """
        n = len(adj_list)
        adj = [[] for _ in range(n+2)]
        # 順辺、逆辺をはる
        for i, elm in enumerate(adj_list):
            for j in elm:
                # 0-index のノードを 1-index 風に変更
                # どちらのエッジからも逆辺への参照を行えるようにしておく
                forward = Edge(i+1, j+1, 1, None)
                backward = Edge(j+1, i+1, 0, forward)
                forward.rev_edge = backward
                adj[i+1].append(forward)
                adj[j+1].append(backward)
        # 超入口、出口を作成し辺をはる
        start_ind = 0
        for i in range(0, n, 2):
            # 0-index のノードを 1-index 風に変更
            forward = Edge(start_ind, i+1, 1, None)
            backward = Edge(i+1, start_ind, 0, forward)
            forward.rev_edge = backward
            adj[start_ind].append(forward)
            adj[i+1].append(backward)
        goal_ind = n + 1
        for i in range(1, n, 2):
            # 0-index のノードを 1-index 風に変更
            forward = Edge(i+1, goal_ind, 1, None)
            backward = Edge(goal_ind, i+1, 0, forward)
            forward.rev_edge = backward
            adj[i+1].append(forward)
            adj[goal_ind].append(backward)
        # import pprint
        # pprint.pprint(adj)
        def dfs():
            path = [Edge(None, start_ind, None, None)]    # 擬似エッジ
            visited = [False] * (n+2)
            visited[start_ind] = 0
            while path:
                previous_e = path[-1]
                u = previous_e.to
                visited[u] = True
                if u == goal_ind:
                    return path[1:]    # 最初の擬似エッジを取り除く
                for e in adj[u]:
                    if not visited[e.to] and e.weight > 0:
                        path.append(e)
                        break
                else:
                    path.pop()
        def update_flow(path):
            maximum_flow = float('inf')
            for e in path:
                maximum_flow = min(maximum_flow, e.weight)
            for e in path:
                e.weight -= maximum_flow    # エッジクラスは参照で渡されているので adj にも変更が反映される
                e.rev_edge.weight += maximum_flow    # どれくらい押し戻せるかが更新される
            return maximum_flow
        # main loop
        flow = 0
        while True:
            # for e in adj:
            #     print(e)
            p = dfs()
            if not p:
                return flow
            else:
                flow += update_flow(p)
                # print(f"path: {list(map(lambda x: x.to - 1, p))[:-1]}, current flow: {flow}")
        

    n = ii()
    red = [lmi() for _ in range(n)]  # 0, 2, 4, 6, ...
    blue = [lmi() for _ in range(n)]  # 1, 3, 5, 7, ...
    # 二部グラフ
    adj = [[] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if red[i][0] < blue[j][0] and red[i][1] < blue[j][1]:
                adj[i*2].append(j*2+1)
    # import pprint
    # pprint.pprint(adj)

    
    print(bipartite_max_matching(adj))
    

    



if __name__ == "__main__":
    main()
