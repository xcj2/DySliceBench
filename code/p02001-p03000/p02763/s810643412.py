#!/usr/bin/env python3

import sys
# import math
# import re                                    # re.compile(pattern) => ptn obj; p.search(s), p.match(s), p.finditer(s) => match obj; p.sub(after, s)
# from collections import deque                # deque class. deque(L): dq.append(x), dq.appendleft(x), dq.pop(), dq.popleft(), dq.rotate()
from collections import defaultdict          # subclass of dict. defaultdict(facroty)
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

    # 各クエリでの O(|alphabet|) が重いため TLE
    # a...z までの出現フラグを bit field で管理することを考える。そうすればある区間での出現文字を管理する数字たちを合わせる際には OR をとるだけて O(1) で高速に処理できる


    class SegTree:
        def __init__(self, size):
            self.size = size
            self.n0 = 2 ** (size - 1).bit_length()
            self.table = [0 for _ in range(2 * self.n0)]
        
        def update(self, k, new_char):
            'update char in a_k to new_char'
            table_k = k + self.n0 - 1
            new_num = 1 << (ord(new_char) - ord('a'))
            if self.table[table_k] != new_num:
                self.table[table_k] = new_num
                while table_k // 2 > 0:
                    table_k //= 2
                    self.table[table_k] = self.table[2 * table_k] | self.table[2 * table_k + 1]
        
        def range_set(self, l, r):
            'return integer that represents character set appeared in a_l to a_r'
            bit_field = 0
            table_l = l + self.n0 - 1
            table_r = r + self.n0 - 1
            if table_l > table_r:
                raise RuntimeError("l should be less than or equals to r. got l:{} and r:{}".format(l, r))
            while table_l < table_r:
                if table_l & 0b1 == 1:
                    bit_field |= self.table[table_l]
                if table_r & 0b1 == 0:
                    bit_field |= self.table[table_r]
                table_l = (table_l + 1)  // 2
                table_r = (table_r - 1) // 2
            if table_l == table_r:
                bit_field |= self.table[table_l]
            return bit_field


    def execute_query(seg_tree, L, buf):
        id = int(L[0])
        if id == 1:
            i = int(L[1])
            char = L[2]
            seg_tree.update(i, char)
        else:
            i, j = map(int, L[1:])
            bit_field = seg_tree.range_set(i, j)
            buf.append(bin(bit_field)[2:].count('1'))

    n = ii()
    s = input()
    q = ii()
    commands = []
    for _ in range(q):
        commands.append(input().split())

    st = SegTree(n)
    for i, char in enumerate(s):
        st.update(i+1, char)
    
    buf = []
    for query in commands:
        execute_query(st, query, buf)
    for elm in buf:
        print(elm)


if __name__ == "__main__":
    main()
