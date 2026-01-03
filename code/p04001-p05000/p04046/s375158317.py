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
    
    
    def make_factorial_table(size, mod):
        '''
        fact_mod[i] は i! % mod を表す。fact_mod[0] ~ facto_mod[size] まで計算可能なテーブルを返す
        >>> make_factorial_table(20, 10**9+7)
        [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 227020758, 178290591, 674358851, 789741546, 425606191, 660911389, 557316307, 146326063]
        '''
        fact_mod = [1] * (size + 1)
        for i in range(1, size + 1):
            fact_mod[i] = (fact_mod[i - 1] * i) % mod
        return fact_mod

    def combination(n, r, mod, fact_table):
        '''
        フェルマーの小定理 
        a ^ p-1 ≡ 1 (mod p)
        a ^ p-2 ≡ 1/a (mod p) (逆元)
        nCr = (n!) / ((n-r)! * r!) だが、mod p の世界ではこの分母を逆元を用いて計算しておくことが可能
        
        >>> m = 1000000007
        >>> fact_table = make_factorial_table(100, m)
        >>> combination(10, 5, m, fact_table)
        252
        >>> combination(100, 50, m, fact_table)
        538992043
        '''
        numerator = fact_table[n]
        denominator = (fact_table[n-r] * fact_table[r]) % mod
        # pow はすでに繰り返し二乗法で効率的に実装されている
        return (numerator * pow(denominator, mod-2, mod)) % mod

    h, w, a, b = mi()
    # sigma {k = b to w-1} h-1-a+kCh-1-a * a-1+w-1-kCa-1
    # sample 2 だと {k=4to6} 6+kC6 * 2+6-kC2 = (10C6 * 4C2 + 11C6 * 3C2 + 12C6 * 2C2)
    fact_table = make_factorial_table(2 * h + 2 * w, mod)
    ans = 0
    for k in range(b, w):
        # print(f"{h-1-a+k} {h-1-a} / {a-1+w-1-k} {a-1}")
        ans = (ans + combination(h-1-a+k, h-1-a, mod, fact_table) * combination(a-1+w-1-k, a-1, mod, fact_table)) % mod
    print(ans)


if __name__ == "__main__":
    main()
