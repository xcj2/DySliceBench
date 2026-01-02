# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
#import math
#from itertools import product, accumulate, combinations, product
#import bisect# lower_bound etc
#import numpy as np
#from copy import deepcopy
#from collections import deque

import math
class segtree:
    def __init__(self, n, init_val = None, init = 0):
        self.n = n
        self.init_val = init_val
        self.init = init
        self.k = math.ceil(math.log2(n))

        try:init_val[0]
        except:raise ValueError('init_val should be list')

        self.bins = [self.init] * (1<<(self.k+1))
        for idx, i in enumerate(range(1<<self.k, 1<<(self.k+1))):
            if len(self.init_val)>idx:
                self.bins[i] = init_val[idx]

        self.caliculate()

    def compare(self, l, r):
        # modify!!
        #print(l, r)
        return max(l, r, key = lambda x:x[0])

    def caliculate(self):
        k = self.k
        while k:
            for i in range(1<<k, 1<<(k+1)):
                if not i%2:
                    self.bins[i//2] = self.compare(self.bins[i], self.bins[i+1])
                else:continue
            k -= 1

    def update(self, idx, val):
        '''idx : 0-started index'''
        k = (1<<self.k) + idx
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

    def value(self, ind):
        return self.bins[(1<<self.k) + ind]


def run():
    N,M = map(int, sysread().split())
    A = list(map(int, sysread().split()))
    A_with_idx = [(a, i) for i, a in enumerate(A)]
    st = segtree(len(A_with_idx), init_val = A_with_idx, init = (0, -1))
    for i in range(M):
        a, idx = st.bins[1]
        st.update(idx, (a // 2, idx))

    ret = 0
    for i in range(N):
        ret += st.value(i)[0]
    print(ret)



if __name__ == "__main__":
    run()
