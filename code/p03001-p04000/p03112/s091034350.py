#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
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
from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
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
    
    
    a, b, q = mi()
    shrine = [ii() for _ in range(a)]
    temple = [ii() for _ in range(b)]
    query = [ii() for _ in range(q)]

    shrine.sort()
    temple.sort()

    for x in query:
        ans = inf
        # print('')
        # 右にのみ進む
        if x <= shrine[-1] and x <= temple[-1]:
            dist = max(abs(x - shrine[bisect_left(shrine, x)]), abs(x - temple[bisect_left(temple, x)]))
            # print(dist)
            ans = min(ans, dist)
        # 左にのみ進む
        if shrine[0] <= x and temple[0] <= x:
            dist = max(abs(x - shrine[bisect_right(shrine, x) - 1]), abs(x - temple[bisect_right(temple, x) - 1]))
            # print(dist)
            ans = min(ans, dist)
        # 右で神社、左で寺を見つける
        if x <= shrine[-1] and temple[0] <= x:
            a = abs(x - shrine[bisect_left(shrine, x)])
            b = abs(x - temple[bisect_right(temple, x) - 1])
            dist = a + b + min(a, b)
            # print(dist)
            ans = min(ans, dist)
        # 右で寺、左で神社を見つける
        if x <= temple[-1] and shrine[0] <= x:
            a = abs(x - temple[bisect_left(temple, x)])
            b = abs(x - shrine[bisect_right(shrine, x) - 1])
            dist = a + b + min(a, b)
            # print(dist)
            ans = min(ans, dist)
        
        # print('ans')
        print(ans)


if __name__ == "__main__":
    main()
