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
from bisect import bisect_left, bisect_right # bisect_left(a, x, lo=0, hi=len(a)) returns i such that all(val<x for val in a[lo:i]) and all(val>-=x for val in a[i:hi]).
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
    
    
    s = input()
    t = input()

    # 構成不可能な場合
    set_s = set(s)
    for char_t in t:
        if char_t not in set_s:
            print(-1)
            exit()

    # 構成可能な場合    
    # 前処理 O(n)
    s_table = [[] for _ in range(ord('z') - ord('a') + 1)]
    for i, s_char in enumerate(s):
        s_table[ord(s_char) - ord('a')].append(i)
    # print(s_table)
    # O(nlgn)
    loop_count = 0
    prev = -1
    for t_char in t:
        candidate = s_table[ord(t_char) - ord('a')]
        j = bisect_left(candidate, prev+1)    # prev より大きくないとだめ
        if j == len(candidate):
            loop_count += 1
            prev = candidate[0]
        else:
            prev = candidate[j]
    print(prev + loop_count * len(s) + 1)


if __name__ == "__main__":
    main()

    """
    解説
    俺の二分探索の方針以外にも「ある index 以降で次に char(a-z) が出現する index を O(alpha)*O(|s|) で求めておく」と言った方法がある。
    こちらは O(|s|) + O(alpha) * O(|s|) + O(|t|)
    二分探は O(|s|) + O(lg|s|) * O(|t|)
    O(alpha) = 26, O(lg|10**5|) = 16, O(|s|) = O(|t|) より今回最悪計算量に変わりはない

    s を二つ連結した文字列を用意して調べると楽らしい。確かに。(必ず探索場所がヒットするので)
    """