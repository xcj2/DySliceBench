#!/usr/bin/env python3

import sys
# import math
# from string import ascii_lowercase, ascii_upper_case, ascii_letters, digits, hexdigits
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
from operator import itemgetter              # itemgetter(1), itemgetter('key')
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
    
    
    # n, m = mi()
    # edge = set()
    # for _ in range(m):
    #     a, b = mi_0()
    #     edge.add((a, b - 1))
    
    # cnt = 0
    # while edge:
    #     accum = [0] * n
    #     for start, end in edge:
    #         accum[start] += 1
    #         accum[end + 1] -= 1
    #     prev = 0
    #     covered_edge_max = 0    # 現時点で残されているインターバルについて最もかぶっているようなポイントを探す。その被っているインターバルの個数
    #     point_x = 0    # そのポイントの座標
    #     for i in range(n):
    #         accum[i] += prev
    #         prev = accum[i]
    #         if accum[i] > covered_edge_max:
    #             covered_edge_max = accum[i]
    #             point_x = i
    #     # print(accum)
    #     cnt += 1
    #     tmp = copy(edge)
    #     for elm in edge:
    #         start, end = elm
    #         if start <= point_x <= end:
    #             tmp.remove(elm)
    #     edge = tmp
    #     print(edge)
    # print(cnt)
    """
    橋を [x_left, x_left + 1) の整数座標区間と考える
    (0-index で) 頂点 i から j へ行けなくする = [i, j) の整数座標区間とかぶるような橋を選択する
    全ての要望 m 個について [i, j) の整数座標区間を用意し、それらと最も被っているような橋を選択 -> 削除 & それにより条件が満たされた整数座標区間も削除...
    を貪欲で行えれば行ける気がしたが嘘貪欲 (半分くらい WA)、TLE
    """

    n, m = mi()
    edge = []
    for _ in range(m):
        a, b = mi()
        edge.append((a, b - 1))
    edge.sort(key=itemgetter(0))

    cnt = 0
    # (未カウントの) これまでの整数座標区間をカバーできる区間をメモする
    prev_left = n + 1
    prev_right = n
    for start, end in edge:
        if start > prev_right:
            cnt += 1
            prev_left = start
            prev_right = end
        # 包含 or ずれているパターン
        else:
            prev_left = start
            prev_right = min(prev_right, end)

    # edge さえあれば必ず +1 されて欲しい (最後に区間が余るので)
    if prev_left <= prev_right:
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
