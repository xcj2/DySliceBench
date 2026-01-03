#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits
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


    def contained_in_dict_set(d, i, j):
        if i in d:
            if j in d[i]:
                return True
        return False
    
    def register_dict_set(d, i, j):
        if i not in d:
            d[i] = set()
        d[i].add(j)

    def count_black_around_center(point_dict, i, j):
        cnt = 0
        for s in range(i-1, i+2):
            for t in range(j-1, j+2):
                if contained_in_dict_set(point_dict, s, t):
                    cnt += 1
        return cnt
    

    h, w, n = mi()
    points = [lmi() for _ in range(n)]
    num_of_grids_contains_black = [0] * 10

    point_dict = dict()
    visited_dict = dict()

    for x, y in points:
        register_dict_set(point_dict, x, y)

    for x, y in points:
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 2<=i<=h-1 and 2<=j<=w-1 and not contained_in_dict_set(visited_dict, i, j):
                    cnt = count_black_around_center(point_dict, i, j)
                    num_of_grids_contains_black[cnt] += 1
                    register_dict_set(visited_dict, i, j)
    
    num_of_grids_contains_black[0] = (h - 2) * (w - 2) - sum(num_of_grids_contains_black[1:])
    print(*num_of_grids_contains_black, sep='\n')    



if __name__ == "__main__":
    main()
