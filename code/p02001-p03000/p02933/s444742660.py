#!/usr/bin/env python3

import sys
# import math
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
    mod = 10000007                  # 10^9+7
    inf = float('inf')
    input = sys.stdin.readline      # 改行文字が残ることに注意
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def ii():  return int(input())
    def mi():  return map(int, input().rstrip().split())
    def lmi(): return list(map(int, input().rstrip().split()))
    def li():  return list(input().rstrip())
    
    
    n = ii()
    s = input().rstrip()
    print(s) if n >= 3200 else print("red")


if __name__ == "__main__":
    main()