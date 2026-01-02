#!/usr/bin/env python3

import sys
# import math
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
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
# from fractions import gcd                    # for Python 3.4


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
    

    def reverse_bisect(L, key):
        """
        L は単調減少
        key 未満となる最初の index を返す
        - left は常に key 未満の条件を満たさない
        - right は常に key 未満の条件を満たす
        - right - left で表される区間幅が 1 になるまで狭める。right が答えになる。
        """
        left = -1
        right = len(L)
        while right - left > 1:
            mid = left + (right - left) // 2
            if L[mid] < key:
                right = mid
            else:
                left = mid
        return right

    
    # 広義最大減少部分列の長さが答え
    n = ii()
    L = [ii() for _ in range(n)]
    # dp[i] には長さ i+1 の広義減少部分列を作った時、末尾の値が最大となるものの値のメモがなされる
    # dp は広義単調減少
    dp = [-float('inf')] * n
    for elm in L:
        insert_ind = reverse_bisect(dp, elm)
        dp[insert_ind] = elm

    prev = -1
    for i, tail_max in enumerate(dp):
        if tail_max == -float('inf'):
            # dp[prev] が メモられてる最後の要素。長さ prev + 1 の広義減少部分列まで作成可能である。
            break
        prev = i
    print(prev + 1)



if __name__ == "__main__":
    main()