#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product, permutations  # product(iter, repeat=n), permutations(iter[,r])
# from itertools import combinations, combinations_with_replacement
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict (e.g. list is not allowed)
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference
# from fractions import gcd                    # for Python 3.4 (previous contest @AtCoder)


def main():
    mod = 1000000007                # 10^9+7
    inf = float('inf')              # sys.float_info.max = 1.79...e+308
    # inf = 2 ** 64 - 1               # (for fast JIT compile in PyPy) 1.84...e+19
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():    return int(input())
    def mi():    return map(int, input().split())
    def mi_0():  return map(lambda x: int(x)-1, input().split())
    def lmi():   return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():    return list(input())
    
    
    # n, m = mi()
    # inv_adj = [set() for _ in range(n)]
    # inv_dist_2 = [set() for _ in range(n)]
    # inv_hopstepjump = [set() for _ in range(n)]

    # for _ in range(m):
    #     u, v = mi_0()
    #     inv_adj[v].add(u)
    
    # for i in range(n):
    #     for s in inv_adj[i]:
    #         inv_dist_2[i] |= inv_adj[s]
        
    # for i in range(n):
    #     for s in inv_dist_2[i]:
    #         inv_hopstepjump[i] |= inv_adj[s]

    # start, goal = mi_0()

    # appeared_vertice_set = set([goal])
    # q = deque([(goal, 0)])
    # while q:
    #     # print(q)
    #     u, turn = q.popleft()
    #     if turn >= n:
    #         break
    #     if u == start:
    #         print(turn)
    #         exit()
    #     for v in inv_hopstepjump[u]:
    #         if v not in appeared_vertice_set:
    #             appeared_vertice_set.add(v)
    #             q.append((v, turn + 1))
    # print(-1)

    """
    set を作るところで最悪 O(n^2) より 2 つくらい TLE
    経路長 3 の倍数というところで start からの経由数の剰余 (mod 3) を管理する、という方針は思いついたが... それをノードを増やすことで管理するという発想に至らず。
    """
    n, m = mi()
    adj = [[] for _ in range(n * 3)]
    for _ in range(m):
        a, b = mi_0()
        adj[a * 3].append(b * 3 + 1)
        adj[a * 3 + 1].append(b * 3 + 2)
        adj[a * 3 + 2].append(b * 3)
    
    start, goal = mi_0()
    start *= 3
    goal *= 3

    q = deque([(start, 0)])
    visited = [False] * (n * 3)
    while q:
        u, dist = q.popleft()
        if dist > 3 * n:
            break
        if u == goal:
            assert (dist % 3 == 0)
            print(dist // 3)
            return
        if not visited[u]:
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    q.append((v, dist + 1))
    print(-1)

        

if __name__ == "__main__":
    main()