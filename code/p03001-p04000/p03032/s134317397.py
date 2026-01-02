#!/usr/bin/env python3

import sys
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import product                # product(iter, repeat=n)
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from fractions import gcd                    # for Python3.4.3
import math

def main():
    mod = 10000007                  # 10^9+7
    inf = float('inf')
    input = sys.stdin.readline      # 改行文字が残ることに注意
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def ii():  return int(input())
    def mi():  return map(int, input().rstrip().split())
    def lmi(): return list(map(int, input().rstrip().split()))
    def li():  return list(input().rstrip())
    
    
    n, k = mi()
    v = lmi()
    # i ... トータルの操作の回数。0 to k 回が許されている
    # 2n 回以上操作を行う意味はない。(2n 回で任意のレパートリーにできる)
    ans = -inf
    k = min(2*n, k)
    for i in range(k+1):    # O(10**2)
        for get_num in range(math.ceil(i/2), min(i+1, n+1)):    # O(50)
            return_num = i - get_num
            # print(f"get{get_num} ret{return_num} tot{i}")
            for from_left in range(get_num+1):    # O(75)
                from_right = get_num - from_left
                # print(f"left{from_left} right{from_right}")
                if from_right == 0:
                    L = v[:from_left]
                else:
                    L = v[:from_left] + v[-from_right:]
                ans = max(ans, sum(sorted(L)[return_num:]))    # O(xlgx (x=0 to 100))
    print(ans)




if __name__ == "__main__":
    main()