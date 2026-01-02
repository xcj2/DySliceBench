# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7

class segtree:
    '''init_val : i-indexed (init_val[0] = self.bin[1])'''
    def __init__(self, n, init = 0, init_val=None):
        self.n = n
        self.init = init
        self.k = math.ceil(math.log2(n))
        self.add_val = 1 << self.k

        try:
            init_val[0]
        except:
            raise ValueError('init_val should be list')

        self.bins = [self.init] * (1 << (self.k + 1))
        if init_val != None:
            self.update_set(init_val)
        self.caliculate()

    def __getitem__(self, idx):  # return idx-value
        return self.bins[idx + self.add_val]

    def update_set(self, vals):
        for idx, i in enumerate(range(self.add_val, self.add_val * 2)):
            if len(vals) > idx:
                self.bins[i] = vals[idx]
            else:continue

    def compare(self, l, r):
        return min(l ,r)

    def caliculate(self):
        k = self.k
        while k:
            for i in range(1<<k, 1<<(k+1)):
                if not i%2:
                    self.bins[i//2] = self.compare(self.bins[i], self.bins[i+1])
                else:continue
            k -= 1

    def update(self, idx, val, by=True):
        '''idx : 0-started index'''
        k = (1<<self.k) + idx
        if by:
            self.bins[k] += val
        else:
            self.bins[k] = val
        while k>1:
            self.bins[k // 2] = self.compare(self.bins[k // 2 * 2], self.bins[k // 2 * 2 + 1])
            k = k//2


    def eval(self, l, r):
        ret = self.init
        l = (1 << self.k) + l
        r = (1 << self.k) + r
        #print(l, r)
        while True:
            #print(l, r)
            if r - l == 1:
                ret = self.compare(ret, self.bins[l])
                ret = self.compare(ret, self.bins[r])
                break
            elif l == r:
                ret = self.compare(ret, self.bins[l])
                break
            else:
                done = False
                if l % 2:
                    ret = self.compare(ret, self.bins[l])
                    l += 1
                    done = True
                if not r % 2:
                    ret = self.compare(ret, self.bins[r])
                    r -= 1
                    done = True
                if not done:
                    l = l // 2
                    r = r // 2
        #print(ret)
        return ret

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

def run():
    H,W = map(int, sysread().split())
    tree = std_map(W, 0)
    for i in range(1, W+1):
        #print(tree.bit.bins)
        tree[i] = 0
    #print(tree.bit.bins)
    arr = [0] * (W+1)
    arr[0] = INF
    moves = segtree(W+1, init=INF, init_val=arr)

    for i in range(1, H+1):
        a, b = map(int, sysread().split())
        k = tree.upper_bound(a-1)
        min_val = INF
        while k <= b:
            min_val = min(b + 1 - k + moves[k], min_val)
            moves.update(k, INF, by=False)
            tree.remove(k)
            k = tree.upper_bound(a-1)
        if b+1 <= W and min_val < moves[b+1]:
            moves.update(b + 1, min_val, by=False)
            tree[b+1] = 1

        if moves.bins[1] == INF:
            print(-1)
        else:
            print(moves.bins[1] + i)




if __name__ == "__main__":
    run()
