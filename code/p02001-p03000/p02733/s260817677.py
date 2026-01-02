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
    
    
    h, w, k = mi()
    L = []
    for _ in range(h):
        L.append(list(map(int, li())))
    L_trans = [[None] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            L_trans[j][i] = L[i][j]
    d = 2 ** (h-1)
    cost = [float('inf')] * d
    for state in range(d):
        bit_count = bin(state)[2:].count('1')
        separated = [[0] * (bit_count + 1) for _ in range(w)]
        for i in range(w):
            current = 0
            for j in range(h):
                if j >= 1 and 1 << (j-1) & state:
                    current += 1
                if L_trans[i][j]:
                    separated[i][current] += 1
        previous = [0] * (bit_count + 1)
        cnt = 0
        # print(separated)
        for i in range(w):
            if any(map(lambda x: x > k, separated[i])):
                break
            if all(map(lambda x: x <= k, [elm + previous[ind] for ind, elm in enumerate(separated[i])])):
                # print(f"just add: {previous} {separated[i]}")
                for ind, elm in enumerate(separated[i]):
                    previous[ind] += elm    # 追加
            else:
                cnt += 1
                # print(f"count up: {previous} {separated[i]}")
                for ind, elm in enumerate(separated[i]):
                    previous[ind] = elm    # 上書き
        else:
            cost[state] = bit_count + cnt
    # print(cost)
    print(min(cost))
                

if __name__ == "__main__":
    main()
