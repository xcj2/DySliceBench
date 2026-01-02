#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

class BinaryIndexedTree:
    def __init__(self, size):
        """
        :param int size:
        """
        self.bit = [0 for _ in range(size)]
        self.size = size
 
    def add(self, i, w):
        """
        i番目にwを加える
        :param int i:
        :param int w:
        :return:
        """
        x = i + 1
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return
 
    def sum(self, i):
        """
        [0,i]の合計
        :param int i:
        :return:
        """
        res = 0
        x = i + 1
        while x > 0:
            res += self.bit[x - 1]
            x -= x & -x
        return res
 
    def search(self, x):
        """
        二分探索。和がx以上となる最小のインデックス(>= 1)を返す
        :param int x:
        :return :
        """
        i = 1
        s = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            if i + step <= self.size and s + self.bit[i + step - 1] < x:
                i += step
                s += self.bit[i - 1]
            step >>= 1
        return i
 
    def __len__(self):
        return self.size

n, q = LI()
c = LI()
lr = [LI() + [i] for i in range(q)]
lr.sort(key=itemgetter(1))
last = [-1] * (n+1)
ans = [0]*q
BIT = BinaryIndexedTree(n+1)
R = 0
for l, r, i in lr:
    while R < r:
        if last[c[R]] >= 0:
            BIT.add(last[c[R]], -1)
        last[c[R]] = R+1
        BIT.add(R+1, 1)
        R += 1
    ans[i] = BIT.sum(r) - BIT.sum(l-1)
for i in ans:
    print(i)
    
    