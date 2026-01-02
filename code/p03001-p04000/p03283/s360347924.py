#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
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
    
    
    n, m, q = mi()
    intervals = []
    for _ in range(m):
        l, r = mi()
        intervals.append((l - 1, r))
    intervals.sort(key=itemgetter(1))

    commands = []
    for _ in range(q):
        a, b = mi()
        commands.append((a - 1, b))

    
    # completely_included[i] = ([0:i] で完全に含んでいる区間数)
    completely_included = [0] * (n + 1)
    for _, right in intervals:
        completely_included[right] += 1
    prev = 0
    for i in range(1, n + 1):
        completely_included[i] += prev
        prev = completely_included[i]
    # print(completely_included)
    
    # across_num[r][l] = (0:right に含まれるインターバルのうち、left を内部に含むようなインターバルの個数)
    across_num = [[0] * (n + 1) for _ in range(n + 1)]
    for left, right in intervals:
        if right - left >= 2:
            for i in range(right, n + 1):
                across_num[i][left + 1] += 1
                across_num[i][right] -= 1
    for i in range(1, n + 1):
        prev = 0
        for j in range(1, n + 1):
            across_num[i][j] += prev
            prev = across_num[i][j]
    

    def calc_included_intervals(left, right):
        return completely_included[right] - completely_included[left] - across_num[right][left]


    for l, r in commands:
        print(calc_included_intervals(l, r))


if __name__ == "__main__":
    main()
