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
    

    def alpha_to_num(s):
        """
        >>> alpha_to_num('AAA')
        0
        >>> alpha_to_num('AGC')
        11
        >>> alpha_to_num('CCC')
        63
        """
        assert(len(s) == 3)
        d = {'A':0, 'T':1, 'G':2, 'C':3}
        num = 0
        for i in range(3):
            num += pow(4, 2 - i) * d[s[i]]
        return num
    
    def num_to_alpha(num):
        """
        >>> num_to_alpha(0)
        'AAA'
        >>> num_to_alpha(11)
        'AGC'
        >>> num_to_alpha(63)
        'CCC'
        """
        assert(0 <= num < 4 ** 3)
        d = {0:'A', 1:'T', 2:'G', 3:'C'}
        L = []
        for i in range(2, -1, -1):
            q = num // pow(4, i)
            L.append(d[q])
            num -= pow(4, i) * q
        return ''.join(L)
    

    def distribute(num, s, num_of_pattern, seq):
        """
        最後の 3 文字が s (数字に直すと num) であるようなものに対し、末尾に A T G C を追加することを考える
        valid pattern を数え上げ、seq の適切な位置にパターンを加算する
        """
        for char in ['A', 'T', 'G', 'C']:
            new_s = s[1:] + char
            new_num = alpha_to_num(new_s)
            if char == 'G':
                if new_s == 'ACG':
                    continue
            elif char == 'C':
                if s in ['AGT', 'AGG', 'ATG']:
                    continue
                if new_s in ['AGC', 'GAC']:
                    continue
            seq[new_num] = (seq[new_num] + num_of_pattern) % mod

    
    n = ii()
    # a:0, t:1, g:2, c:3 とする
    # dp[i][num] = (i 文字で末尾の 4 進数表記が num となる適切な文字列の数)
    dp = [[0] * (4 ** 3) for _ in range(n + 1)]
    
    for num in range(4 ** 3):
        dp[3][num] = 1 if num_to_alpha(num) not in ['AGC', 'ACG', 'GAC'] else 0
    
    for i in range(3, n):
        # dp[i] は既知。dp[i+1] に配る
        for num in range(4 ** 3):
            distribute(num, num_to_alpha(num), dp[i][num], dp[i+1])


    print(sum(dp[n]) % mod)


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    main()
