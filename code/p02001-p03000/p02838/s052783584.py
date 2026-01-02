#!/usr/bin/env pypy3

import sys
import math
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
# from collections import defaultdict          # subclass of dict. defaultdict(facroty)
# from collections import Counter              # subclass of dict. Counter(iter): c.elements(), c.most_common(n), c.subtract(iter)
# from heapq import heapify, heappush, heappop # built-in list. heapify(L) changes list in-place to min-heap in O(n), heappush(heapL, x) and heappop(heapL) in O(lgn).
# from heapq import nlargest, nsmallest        # nlargest(n, iter[, key]) returns k-largest-list in O(n+klgn).
# from itertools import product                # product(iter, repeat=n)
# from itertools import accumulate             # accumulate(iter[, f])
# from functools import reduce                 # reduce(f, iter[, init])
# from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
# from fractions import gcd                    # for Python3.4.3


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
    
    
    n = ii()
    a = lmi()
    m = max(a)
    # corner case: all numbers are equal to zero
    if m == 0:
        print(0)
        exit(0)

    ans = 0
    for shift in range(int(math.log(m, 2)+1)):    # log2 は PyPy2.4.0 で使えない
        mask = 0b1 << shift
        # print(tuple(map(lambda x: (x&mask)>>shift, a)))
        count_one = tuple(map(lambda x: (x&mask)>>shift, a)).count(1)
        ans = (ans + int(pow(2, shift, mod)) * count_one * (n - count_one)) % mod
        # print(ans)
    print(ans)
    # TLE -> random_31 to random_35 system test cases


if __name__ == "__main__":
    main()