#!/usr/bin/env python3

import sys
import math
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
    
    
    n, k = mi()
    A = sorted(lmi(), reverse=True)
    F = sorted(lmi())
    # O(K) * O(lgN)
    # h = [[- A[i] * F[i], F[i]] for i in range(n)]
    # heapify(h)
    # # print(h)
    # for _ in range(k):
    #     minus_val, cost = heappop(h)
    #     plus_val = - minus_val
    #     # plus_val は max heap から取り出した最大値となる
    #     if plus_val == 0:
    #         # もう減らす場所はない。一応戻して抜ける
    #         heappush(h, [plus_val, cost])
    #         break
    #     plus_val -= cost
    #     heappush(h, [- plus_val, cost])
    
    # minus_val, cost = heappop(h)
    # print(- minus_val)

    # O(lgK) * O(N)

    def calc_total_training(A, F, n, key):
        '各メンバーが秒数を key 以下にする必要がある時必要なトレーニングの総数を計算する'
        cnt = 0
        if key < 0:
            return float('inf')
        else:
            for i in range(n):
                diff = max(A[i] * F[i] - key, 0)
                cnt += math.ceil(diff / F[i])
            return cnt
    
    def is_ok(A, F, n, k, key):
        'k 回以下のトレーニングで各メンバーが秒数を key 以下にすることは可能か判定する'
        return calc_total_training(A, F, n, key) <= k
    
    def meguru_bisect(A, F, n, k):
        'k 回以下のトレーニングで達成可能な最短秒数を求める'
        left_sec = -1    # 必ず達成不可能
        right_sec = 10 ** 12    # 必ず達成可能
        while right_sec - left_sec > 1:
            mid = left_sec + (right_sec - left_sec) // 2
            if is_ok(A, F, n, k, mid):
                right_sec = mid
            else:
                left_sec = mid
        return right_sec
    
    print(meguru_bisect(A, F, n, k))



if __name__ == "__main__":
    main()
