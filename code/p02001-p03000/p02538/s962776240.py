# coding: utf-8
import sys

# from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
import math
# from itertools import product, accumulate, combinations, product
#import bisect
# import numpy as np
# from copy import deepcopy
#from collections import deque
# from decimal import Decimal
# from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 998244353


def intread():
    return int(sysread())
def mapline(t=int):
    return map(t, sysread().split())
def mapread(t=int):
    return map(t, read().split())

class BIT:
    # init_val[0] -> bins[1]
    def __init__(self, n, init=0, init_val=None):
        '''
        n : length of vals
        init : init_val in each bins
        init_val : if specified, update is performed
        ** applioed seqs -> seq[0] -> bins[1]
        '''
        self.n = n
        self.init = init
        self.k = n.bit_length()
        self.bins = [init] * (n+1)
        self.l2 = 2 ** self.k

        if init_val !=None:
            self.update_set(init_val)

    def update_set(self, vals):
        if len(vals) > self.n:
            raise ValueError('Length is too long!')
        for i, val in enumerate(vals):
            bi = i+1
            if bi & 1:
                self.bins[bi] = val
            else:
                ret = self.init
                most_sig = (bi & -bi)
                n_bit = bi - 1
                while n_bit:
                    v = n_bit & -n_bit
                    if most_sig  >= v:break
                    ret = self.compare(ret, self.bins[n_bit])
                    n_bit -= v
                self.bins[bi] = ret

    def compare(self, l, r):
        '''comparison-criteria'''
        return l+ r

    def minus(self, val):
        '''define the negative value for caliculations'''
        return -val

    def update(self, idx, by):
        '''idx : 0-started index'''
        while idx < len(self.bins):
            self.bins[idx] = self.compare(self.bins[idx], by)
            idx += (idx & -idx)

    def get_sum(self, idx):
        '''idx: 0-indexed'''
        ans = self.init
        #idx += 1
        while idx:
            ans = self.compare(ans, self.bins[idx])
            idx -= (idx & -idx)
        return ans

    def eval_between(self, l, r):
        ''' l, r : 0-indexed '''
        return self.compare(self.get_sum(r), self.get_sum(self.get_sum(l-1)))

    def lower_bound(self, SUM):
        '''return idx sum of which is less or equal to SUM'''
        if SUM <= 0:
            return 0
        l = 0
        r = self.l2
        while r > 0:
            if l+r <= self.n and self.bins[l+r] < SUM:
                SUM -= self.bins[l + r]
                l += r
            r >>= 1
        return l + 1

    def upper_bound(self, SUM):
        '''return idx sum of which is more than SUM'''
        l = 0
        r = self.l2
        #print(r,r,r,r,r)
        while r > 0:
            if l + r <= self.n and self.bins[l + r] <= SUM:
                SUM -= self.bins[l + r]
                l += r
            r >>= 1
        return l + 1

class std_map:
    '''
    std_map function with restricted value range.
    n : max val permitted for map
    init : val if key is not specified
    '''

    def __init__(self, n, init):
        self.size = n
        self.keys = set()
        self.bit = BIT(n + 1)# memory keys
        self.dic = [init] * (n + 1)# memory vals

    def __contains__(self, key):  # keyを持つか
        return key in self.keys

    def __getitem__(self, key):  # keyに対するvalueを返す
        return self.dic[key]

    def __setitem__(self, key, value):  # dic[key]をvalueで置き換える
        if not key in self.keys:
            self.bit.update(key, 1)
            self.keys.add(key)
        self.dic[key] = value

    def remove(self, key):  # keyをmapから取り除く
        self.keys.remove(key)
        self.bit.update(key, -1)

    def lower_bound(self, k):  # k以下の最大のkeyを返す
        return self.bit.lower_bound(self.bit.get_sum(k))

    def upper_bound(self, k):  # kより大きい最小のkeyを返す
        return self.bit.upper_bound(self.bit.get_sum(k))

    def kth_key(self, k):  # k番目に小さいkeyを返す
        return self.bit.lower_bound(k)

    def kth_value(self, k):  # k番目に小さいkeyに対するvalueを返す
        return self.dic[self.kth_key(k)]

    def prev_k(self, k):  # kの一つ前のkeyを返す
        idx = self.bit.get_sum(k)
        if idx == 0:
            return -1
        return self.bit.lower_bound(idx - 1)

def pow_mod(x, k , mod):
    ret = [1]
    a = 1
    for i in range(k):
        a *= x
        a %= mod
        ret.append(a)
    return ret

def run():
    N, Q = mapline()
    m = std_map(N, init = -1)
    m[1] = (N, 1)
    powmod = pow_mod(10, N - 1, mod)
    summod = [0]
    t = 0
    for p in powmod:
        t += p
        summod.append(t)


    ans = summod[N]

    for i in range(Q):
        #print(m.keys)
        l, r, d = mapline()

        s = m.lower_bound(l-1)

        #print(s)
        if s > 0:
            rr, dd = m[s]
            if l <= rr:
                #print(rr - s + 1, N-rr)
                ans -= summod[rr - s + 1] * powmod[N-rr] * dd
                ans %= mod
                m[s] = (l-1, dd)
                ans += summod[l - s] * powmod[N -l + 1] * dd
                ans %=mod
                if r < rr:
                    m[l] = (r, d)
                    ans += summod[r - l + 1] * powmod[N - r] * d
                    ans %= mod
                    m[r+1] = (rr, dd)
                    ans += summod[rr - r] * powmod[N - rr] * dd
                    ans %= mod
                    print(ans)
                    continue

        k = l - 1
        while True:
            s = m.upper_bound(k)
            #print(k, s)
            #print(m.bit.bins)
            if s == N+1:break
            if s <= r:
                rr, dd = m[s]
                m.remove(s)
                ans -= summod[rr - s + 1] * powmod[N - rr] * dd
                ans %= mod
                if rr > r:
                    m[r+1] = (rr, dd)
                    ans += summod[rr - r] * powmod[N - rr] * dd
                    ans %= mod
                    break
                k = rr
            else:
                break
        m[l] = (r, d)
        ans += summod[r - l + 1] * powmod[N - r] * d
        ans %= mod
        print(ans)

if __name__ == "__main__":
    run()
