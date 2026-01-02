#!/usr/bin/env python3

import sys
# import math
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product                # product(iter, repeat=n)
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4


def main():
    mod = 1000000007                  # 10^9+7
    inf = float('inf')
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():  return int(input())
    def mi():  return map(int, input().split())
    def mi_0(): return map(lambda x: int(x)-1, input().split())
    def lmi(): return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():  return list(input())


    class UnionFind:
        def __init__(self, n):
            self.table = [i for i in range(n)]
            self.rank = [0] * n
            self.group_size = [1] * n
        
        def find_root(self, i):
            if self.table[i] == i:
                return i
            root = self.find_root(self.table[i])
            self.table[i] = root    # 経路圧縮
            return root
        
        def is_same(self, x, y):
            return self.find_root(x) == self.find_root(y)
        
        def union(self, x, y):
            s = self.find_root(x)
            t = self.find_root(y)
            if s == t:
                return False
            else:
                if self.rank[s] > self.rank[t]:
                    s, t = t, s
                self.table[s] = t
                self.group_size[t] += self.group_size[s]
                if self.rank[s] == self.rank[t]:
                    self.rank[t] += 1
                return True
        
        def num_of_members(self, i):
            root = self.find_root(i)
            return self.group_size[root]
    

    n, m, k = lmi()
    adj_friend = [[] for _ in range(n)]
    for _ in range(m):
        a, b = mi_0()
        adj_friend[a].append(b)
        adj_friend[b].append(a)
    adj_rival = [[] for _ in range(n)]
    for _ in range(k):
        c, d = mi_0()
        adj_rival[c].append(d)
        adj_rival[d].append(c)
    
    uf = UnionFind(n)
    for i, elm in enumerate(adj_friend):
        for j in elm:
            if i < j:
                uf.union(i, j)
    
    for i in range(n):
        connected = uf.num_of_members(i)
        connected_rival = 0
        for rival in adj_rival[i]:
            if uf.is_same(i, rival):
                connected_rival += 1
        # print(f"{connected} {connected_rival} {len(adj_friend[i])}")
        print(connected - connected_rival - len(adj_friend[i]) - 1, end=' ')    # 自分を引くことを忘れずに
    print('')
    

if __name__ == "__main__":
    main()