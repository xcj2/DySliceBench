# -*- coding: utf-8 -*-
from bisect import bisect, bisect_left
from collections import Counter
from functools import reduce
from itertools import accumulate
from operator import itemgetter, xor

import sys
input = sys.stdin.readline

def inpl(): return list(map(int, input().split()))

class BIT:
    def __init__(self, N):
        # Nは入れたい要素の個数
        self.size = 2 ** (int.bit_length(N+1))
        self.node = [0]*(self.size + 1)
 
    def initialize(self, S):
        # S[0] = 0にしておく
        # 1-indexed
        if len(S) < self.size + 1:
            S += [S[-1]] * (self.size+1 - len(S))
        for i in range(1, self.size+1):
            self.node[i] = S[i] - S[i - (i&-i)]
 
    def sum(self, i):
        res = 0
        while i:
            res += self.node[i]
            i -= (i & -(i))
        return res
 
    def add(self, i, x):
        if i == 0:
            return
        while i <= self.size:
            self.node[i] += x
            i += (i & -(i))
 
    def bisect_left(self, x):
        res = 0
        tmp = 0
        b = 2**(int.bit_length(self.size)-2)
        while b:
            if tmp + self.node[res+b] < x:
                res += b
                tmp += self.node[res]
            b //= 2
        return res + 1
 
    def bisect(self, x):
        res = 0
        tmp = 0
        b = 2**(int.bit_length(self.size)-2)
        while b:
            if tmp + self.node[res+b] <= x:
                res += b
                tmp += self.node[res]
            b //= 2
        return res + 1

class DammySet:

    def __init__(self, counter, INF=2**32, counter_is_unique_and_sorted=True):
        if not counter_is_unique_and_sorted:
            if type(counter) != Counter:
                counter = Counter(counter)

            self.bit = BIT(len(counter.keys())+3)
            self.key = sorted([-INF, -INF] + sorted(counter.keys()) + [INF])
            self.val = [counter[k] for k in self.key]
            S = list(accumulate(self.val))
            self.bit.initialize(S)

        else:
            self.bit = BIT(len(counter) + 3)
            self.key = [-INF] * (len(counter) + 3)
            self.val = [0] * (len(counter) + 3)
            S = [0] * (len(counter) + 3)
            for i in range(2, len(counter)+2):
                self.key[i] = counter[i-2]
                self.val[i] = 1
                S[i] = i-1
            self.key[-1] = INF
            S[-1] = len(counter)
            self.bit.initialize(S)

    def add(self, val):
        ix = bisect_left(self.key, val)
        assert self.key[ix] == val
        self.bit.add(ix, 1)


    def update(self, vals):
        for k, v in Counter(vals).items():
            ix = bisect_left(self.key, k)
            if self.key[ix] != k:
                raise KeyError
            self.bit.add(ix, v)


    def remove(self, vals):
        for k, v in Counter(vals).items():
            ix = bisect_left(self.key, k)
            if self.key[ix] != k:
                raise KeyError
            
            # 空の値を削除しないかのチェック
            # 時間が厳しそうなときはコメントアウト
            assert self.bit.sum(ix) - self.bit.sum(ix-1) > 0

            self.bit.add(ix, -v)


    def pop_vals(self, l, r):
        assert l <= r

        rix = bisect(self.key, r) - 1
        lix = bisect_left(self.key, l) - 1
        # (lix, rix]になるのに注意
        rv = self.bit.sum(rix)
        lv = self.bit.sum(lix)
        delta = rv - lv
        tv = lv+1
        tix = lix*1

        vix = 0
        rmvix = 0
        vals = [0]*delta
        rmvk = [0]*delta
        rmvv = [0]*delta
        while delta:
            OK = self.bit.bisect_left(tv)
            c = self.bit.sum(OK)
            d = c - tv + 1
            for _ in range(d):
                vals[vix] = self.key[OK]
                vix += 1
            rmvk[rmvix] = OK
            rmvv[rmvix] = d
            rmvix += 1
            tv += d
            tix = OK
            delta -= d

        for i in range(rmvix):
            self.bit.add(rmvk[i], -rmvv[i])
        return vals

N, M = inpl()
Q = sorted([inpl() for _ in range(N)], key=itemgetter(2))
D = [int(input()) for _ in range(M)]
rD = {v:i for i, v in enumerate(D)}
ans = [-1]*(M)
 
dmap = DammySet(D)
 
for s, t, x in Q:
    val = dmap.pop_vals(s-x, t-1-x)
    for v in val:
        ans[rD[v]] = x
 
print(*ans, sep="\n")