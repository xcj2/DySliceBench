#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict (e.g. list is not allowed)
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4 (previous contest @AtCoder)


def main():
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79...e+308
    inf = 2 ** 64 - 1               # (for fast JIT compile in PyPy) 1.84...e+19
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())
    

    def edge_to_vertex(n, i, j):
        'convert edge(i,j) (1-index) to vertex'
        return (2 * n - i) * (i - 1) // 2 + (j - i - 1)
    
    def topological_bfs(m, adj):
        sorted_vertices = []
        dim = [0] * m
        for i in range(m):
            for j in adj[i]:
                dim[j] += 1
        q = deque()
        for i in range(m):
            if dim[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            assert(dim[u] == 0)
            sorted_vertices.append(u)
            for v in adj[u]:
                dim[v] -= 1
                if dim[v] == 0:
                    q.append(v)
        return sorted_vertices


    
    n = ii()
    # 試合の組み合わせを頂点へと変換し有向グラフ隣接リストへと変換する前処理 O(n^2)
    m = n * (n - 1) // 2
    adj = [[] for _ in range(m)]
    for i in range(1, n + 1):
        L = lmi()
        vertices = [edge_to_vertex(n, min(i, j), max(i, j)) for j in L]
        for k in range(1, n - 1):
            u, v = vertices[k-1], vertices[k]
            adj[u].append(v)
    # print(adj)

    # BFS トポロジカルソートを用いて閉路判定 O(n^2)
    topological_sorted = topological_bfs(m, adj)
    if len(topological_sorted) != m:
        print(-1)
    # 入次数 0 の頂点からトポロジカルソート順に辺を緩和し、最大距離を返す O(n^2)
    else:
        cost = [1] * m
        for u in topological_sorted:
            for v in adj[u]:
                cost[v] = max(cost[u], cost[u] + 1)
        print(max(cost))
 

if __name__ == "__main__":
    main()
