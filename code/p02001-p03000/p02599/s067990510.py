# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque

INF = 1 << 50


class BIT:
    # init_val[0] -> bins[1]
    def __init__(self, n, init_val, init):
        self.n = n
        self.init_val = init_val
        self.init = init
        self.k = math.ceil(math.log2(n))

        try:
            init_val[0]
        except:
            raise ValueError('init_val should be list')

        self.bins = [self.init] * ((1 << self.k) + 1)
        for i, val in enumerate(self.init_val):
            bi = i + 1
            if bi & 1:
                self.bins[bi] = val
            else:
                ret = self.init
                most_sig = (bi & -bi)
                n_bit = bi - 1
                while n_bit:
                    v = n_bit & -n_bit
                    if most_sig >= v: break
                    ret = self.compare(ret, self.bins[n_bit])
                    n_bit -= v
                self.bins[bi] = ret

    def compare(self, l, r):
        return l + r

    def minus(self, val):
        return -val

    def update(self, idx, by, minus=False):
        '''idx : 0-started index'''
        if minus:
            by = self.minus(by)
        idx += 1
        while idx < len(self.bins):
            self.bins[idx] = self.compare(self.bins[idx], by)
            idx += (idx & -idx)

    def eval(self, idx):
        '''idx: 0-indexed'''
        ans = self.init
        idx += 1
        while idx:
            ans = self.compare(ans, self.bins[idx])
            idx -= (idx & -idx)
        return ans

    def eval_between(self, l, r):
        ''' l, r : 0-indexed '''
        return self.compare(self.eval(r), self.minus(self.eval(l - 1)))

def run():
    N, Q = map(int, sysread().split())
    right_arr = [-1] * (N+1)
    C = list(map(int, sysread().split()))

    L,R = [],[]
    for i in range(Q):
        l,r = map(int, sysread().split())
        L.append((l, i))
        R.append((r, i))
    perms = [i for r,i in sorted(R)]
    ans = [-1] * Q

    bit = BIT(N, init_val = [0]*N, init=0)
    checked = -1
    for perm in perms:
        r, i = R[perm]
        l, _ = L[perm]
        r -= 1
        l -= 1
        #print(l, r)
        for idx, c in enumerate(C[checked+1:r+1], checked+1):
            if right_arr[c] < idx:
                pre_idx = right_arr[c]
                right_arr[c] = idx
                if pre_idx != -1:
                    bit.update(pre_idx, by=1, minus=True)
                bit.update(idx, by=1, minus=False)
                #print(pre_idx, idx, c, seg.bins)
        sub = bit.eval(l-1) if l > 0 else 0
        val = bit.eval(r) - sub
        ans[i] = val
        checked = r
        #print(val)

    for a in ans:
        print(a)




if __name__ == "__main__":
    run()