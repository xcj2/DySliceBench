#!/usr/bin/env python3

import sys
# import math
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import count, cycle, repeat   # count(start[,step]), cycle(iter), repeat(elm[,n])
# from itertools import groupby                # [(k, list(g)) for k, g in groupby('000112')] returns [('0',['0','0','0']), ('1',['1','1']), ('2',['2'])]
# from itertools import starmap                # starmap(pow, [[2,5], [3,2]]) returns [32, 9]
# from itertools import product                # product(iter, repeat=n)
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from functools import lru_cache              # @lrucache ...arguments of functions should be able to be keys of dict
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from copy import deepcopy                    # to copy multi-dimentional matrix without reference


def main():
    mod = 1000000007                  # 10^9+7
    inf = float('inf')
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():  return int(input())
    def mi():  return map(int, input().split())
    def mi_0(): return map(lambda x: int(x)-1, input().split())
    def lmi(): return list(map(int, input().split()))
    def lmi_0(): return list(map(lambda x: int(x)-1, input().split()))
    def li():  return list(input())
    
    # x = 10
    # dp = [[0] * 10 for _ in range(x)]
    # for i in range(0, 10):
    #     dp[0][i] = 1
    # for d in range(1, x):
    #     for i in range(0, 10):
    #         tmp = 0
    #         if i-1 >= 0:
    #             tmp += dp[d-1][i-1]
    #         tmp += dp[d-1][i]
    #         if i+1 <= 9:
    #             tmp += dp[d-1][i+1]
    #         dp[d][i] += tmp
    # print(sum([sum(line[1:]) for line in dp[:x]]))
    """
    この dp で x 桁までの整数で表現される LunLun number の数を sum([line[1:] for line in dp[:x]]) で計算できる
    1 桁まで考えると 9 個
    2 桁まで考えると 35 個
    3 桁まで考えると 110 個
    4 桁まで考えると 327 個
    5 桁まで考えると 956 個
    6 桁まで考えると 2782 個
    7 桁まで考えると 8089 個
    8 桁まで考えると 23527 個
    9 桁まで考えると 68468 個
    10 桁まで考えると 199368 個
    であることがわかる。 k 番目の LunLun number を求める (k = O(10^5)) ので、10 桁の数くらいにはなりうることがわかった。
    ( ˘-з-)ふーん。
    """

    k = ii()
    cnt = 0
    q = deque(list('123456789'))
    while True:
        top = q.popleft()
        cnt += 1
        if cnt == k:
            break
        last_digit = int(top[-1])
        if last_digit - 1 >= 0:
            q.append(top + str(last_digit - 1))
        q.append(top + str(last_digit))
        if last_digit + 1 <= 9:
            q.append(top + str(last_digit + 1))
    print(top)
    """
    Queue を使う！ (解説チラ見 AC)
    """
        

if __name__ == "__main__":
    main()