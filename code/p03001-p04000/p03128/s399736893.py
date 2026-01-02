#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from operator import itemgetter              # itemgetter(1), itemgetter('key')
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
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
from copy import copy, deepcopy                    # to copy multi-dimentional matrix without reference
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
    
    
    n, m = mi()
    A = lmi()
    # A の前処理 (同じ必要本数なのに値が小さいやつらが入っていたら削除しておく)
    if 6 in A and 9 in A:
        A.remove(6)
    if 2 in A and 5 in A:
        A.remove(2)
    if 3 in A and 5 in A:
        A.remove(3)
    if 2 in A and 3 in A:
        A.remove(2)    

    # 各数字とマッチの必要本数の対応テーブル
    num_to_match = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    match_to_num = dict()
    for num in A:
        match_to_num[num_to_match[num]] = num

    
    needed_match = [num_to_match[num] for num in A]

    # dp[i] = (指定された数字を使い i 本全部を使って作れる最大桁数, 使用数字のカウンタ)
    dp = [[None, None] for _ in range(n + 1)]
    dp[0][0] = 0
    dp[0][1] = Counter()

    def counter_gt(c1, c2):
        # print(f"{c1} {c2}")
        return sorted(tuple(c1.items()), key=lambda x: x[0], reverse=True) > sorted(tuple(c2.items()), key=lambda x: x[0], reverse=True)

    for i in range(n + 1):
        digit_max = 0
        counter_memo = None
        for match in needed_match:
            if i - match >= 0 and dp[i - match][0] is not None:
                tmp = copy(dp[i - match][1])
                tmp[match_to_num[match]] += 1
                if dp[i - match][0] + 1 > digit_max or (dp[i - match][0] + 1 == digit_max and counter_gt(tmp, counter_memo)):
                    digit_max = dp[i - match][0] + 1
                    counter_memo = copy(dp[i - match][1])
                    counter_memo[match_to_num[match]] += 1 

        if digit_max != 0:
            dp[i][0] = digit_max
            dp[i][1] = counter_memo

    # print('')
    # for elm in dp:
    #     print(elm)
    
    char_array = [None] * dp[n][0]
    cnt = 0
    t = sorted(dp[n][1].items(), key=lambda x: x[0], reverse=True)
    for k, v in t:
        for i in range(v):
            char_array[i + cnt] = str(k)
        cnt += v
    print(''.join(char_array))




if __name__ == "__main__":
    main()
