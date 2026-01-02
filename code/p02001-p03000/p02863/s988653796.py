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
    
    
    n, t = mi()
    eating_cost = [None]    # 1-index
    energy = [None]    # 1-index
    for _ in range(n):
        a, b = mi()
        eating_cost.append(a)
        energy.append(b)
    
    # dp_cost_until_i[k][i] = (時間コスト k (0<=k<=t-1) 以下で Ai (1<=i<=n) までを使用してエネルギーを最大化した時の値)
    dp_cost_unitl_i = [[0] * (n + 2) for _ in range(t)]
    for time_cost in range(1, t):
        for i in range(1, n + 1):
            tmp = energy[i] + dp_cost_unitl_i[time_cost - eating_cost[i]][i - 1] if time_cost - eating_cost[i] >= 0 else 0
            dp_cost_unitl_i[time_cost][i] = max(dp_cost_unitl_i[time_cost][i - 1], tmp)
    # dp_cost_from_i[k][i] = (時間コスト k (0<=k<=t-1) 以下で Ai (1<=i<=n) からを使用してエネルギーを最大化した時の値)
    dp_cost_from_i = [[0] * (n + 2) for _ in range(t)]
    for time_cost in range(1, t):
        for i in range(n, 0, -1):
            tmp = energy[i] + dp_cost_from_i[time_cost - eating_cost[i]][i + 1] if time_cost - eating_cost[i] >= 0 else 0
            dp_cost_from_i[time_cost][i] = max(dp_cost_from_i[time_cost][i + 1], tmp)
    
    maximum_energy = 0
    for i in range(1, n + 1):
        # Ai が最後に食べるものの時
        for until_i_time in range(t):
            a = dp_cost_unitl_i[until_i_time][i - 1]
            b = dp_cost_from_i[t - 1 - until_i_time][i + 1]
            maximum_energy = max(maximum_energy, energy[i] + a + b)
    
    print(maximum_energy)


if __name__ == "__main__":
    main()
