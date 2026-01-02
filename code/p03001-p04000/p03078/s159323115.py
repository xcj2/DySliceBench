#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
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
    

    def calc_1000_num(a, b, c):
        return a + (10 ** 3) * b + (10 ** 6) * c
    
    x, y, z, k = mi()
    A = sorted(lmi(), reverse=True)
    B = sorted(lmi(), reverse=True)
    C = sorted(lmi(), reverse=True)

    h = [(- (A[0]+B[0]+C[0]), [0, 0, 0])]
    registered = set()
    registered.add(calc_1000_num(0, 0, 0))

    for _ in range(k):
        minus_delicious, indices = heappop(h)
        a, b, c = indices
        print(- minus_delicious)
        if a + 1 < x and calc_1000_num(a + 1, b, c) not in registered:
            heappush(h, (- (A[a+1]+B[b]+C[c]), [a+1, b, c]))
            registered.add(calc_1000_num(a + 1, b, c))
        if b + 1 < y and calc_1000_num(a, b + 1, c) not in registered:
            heappush(h, (- (A[a]+B[b+1]+C[c]), [a, b+1, c]))
            registered.add(calc_1000_num(a, b + 1, c))
        if c + 1 < z and calc_1000_num(a, b, c + 1) not in registered:
            heappush(h, (- (A[a]+B[b]+C[c+1]), [a, b, c+1]))
            registered.add(calc_1000_num(a, b, c + 1))

    


if __name__ == "__main__":
    main()
