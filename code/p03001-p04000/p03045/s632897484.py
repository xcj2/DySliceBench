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
    

    class UnionFindTree:
        def __init__(self, num_of_elm):
            self.n = num_of_elm
            self.table = [i for i in range(self.n)]
            self.rank = [0] * self.n
            self.group_size = [1] * self.n
        
        def _find_set(self, x):
            parent = self.table[x]
            if x == parent:
                return x
            else:
                root = self._find_set(parent)
                # 経路圧縮
                self.table[x] = root
                return root
        
        def is_same(self, x, y):
            return self._find_set(x) == self._find_set(y)

        def union(self, x, y):
            shallow_root = self._find_set(x)
            deep_root = self._find_set(y)
            if self.rank[shallow_root] > self.rank[deep_root]:
                shallow_root, deep_root = deep_root, shallow_root
            # そもそも同一グループだった時
            if shallow_root == deep_root:
                return False
            # グループが異なるので union
            else:
                self.table[shallow_root] = deep_root
                self.group_size[deep_root] += self.group_size[shallow_root]
                # 深さが等しかったときはつけ加えられた側の rank をインクリメントする
                if self.rank[shallow_root] == self.rank[deep_root]:
                    self.rank[deep_root] += 1
                return True

        def akin_num(self, x):
            x_root = self._find_set(x)
            return self.group_size[x_root]

        def print_group_id(self):
            print([self._find_set(x) for x in self.table])    
    

    n, m = mi()
    uf = UnionFindTree(n)
    groups = n
    for _ in range(m):
        x, y, _ = mi()
        x -= 1
        y -= 1
        if uf.union(x, y):
            groups -= 1
    print(groups)

if __name__ == "__main__":
    main()