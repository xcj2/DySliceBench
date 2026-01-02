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

#引用
#https://juppy.hatenablog.com/entry/2019/11/13/%E6%9C%80%E5%A4%A7%E3%83%BB%E6%9C%80%E5%B0%8F%E3%82%BB%E3%82%B0%E6%9C%A8_%E3%82%B3%E3%83%94%E3%83%9A%E7%94%A8_Python

n, k = LI()
a = [I() for _ in range(n)]

def init_max(init_max_val):
    #built
    for i in range(num_max-2,-1,-1) :
        seg_max[i]=max(seg_max[2*i+1],seg_max[2*i+2]) 
    
def update_max(k,x):
    k += num_max-1
    seg_max[k] = x
    while k:
        k = (k-1)//2
        seg_max[k] = max(seg_max[k*2+1],seg_max[k*2+2])
    
def query_max(p,q):
    if q<=p:
        return ide_ele_max
    p += num_max-1
    q += num_max-2
    res=ide_ele_max
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg_max[p])
        if q&1 == 1:
            res = max(res,seg_max[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg_max[p])
    else:
        res = max(max(res,seg_max[p]),seg_max[q])
    return res

#####単位元######
ide_ele_max = 0
ma = max(a)
#num_max:n以上の最小の2のべき乗
num_max =2**(ma-1).bit_length()
seg_max=[ide_ele_max]*2*num_max
init_max(a)
for ai in a:
    res = query_max(max(0, ai-k), min(ai+k+1, num_max))
    update_max(ai, res+1)
print(max(seg_max))