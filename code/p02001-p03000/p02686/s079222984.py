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
    
    
    n = ii()
    l_p_only = []
    r_p_only = []
    r_p_l_p = []
    for _ in range(n):
        s = input()
        left_cnt = 0
        right_cnt = 0
        for char in s:
            if char == ')':
                if left_cnt > 0:
                    left_cnt -= 1
                else:
                    right_cnt += 1
            else:
                left_cnt += 1
        if left_cnt == 0 and right_cnt == 0:
            pass
        elif right_cnt == 0:
            l_p_only.append(left_cnt)
        elif left_cnt == 0:
            r_p_only.append(- right_cnt)
        else:
            r_p_l_p.append([- right_cnt, left_cnt])
    # print(l_p_only)
    # print(r_p_l_p)
    # print(r_p_only)

    current_left = sum(l_p_only)
    pos = []
    neg = []
    for elm in r_p_l_p:
        if elm[0] + elm[1] >= 0:
            pos.append(elm)
        else:
            neg.append(elm)
    pos.sort(key=lambda x: x[0], reverse=True)    # 負の値が大きい順、0 に近い順
    for elm in pos:
        current_left += elm[0] 
        if current_left >= 0:
            current_left += elm[1]
        else:
            print('No')
            exit()
    neg.sort(key=lambda x: x[0])    # 負の値が小さい順、- に大きい順に最初のうちにやっておく
    for elm in neg:
        current_left += elm[0]
        if current_left >= 0:
            current_left += elm[1]
        else:
            print('No')
            exit()
    if current_left >= 0 and current_left == - sum(r_p_only):
        print('Yes')
    else:
        print('No')



if __name__ == "__main__":
    main()
