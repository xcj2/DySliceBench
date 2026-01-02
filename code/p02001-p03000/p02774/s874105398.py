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


def f(x): # x以下のペアがk個以上あるかどうかを返す関数
    cnt = 0
    if x < 0: # xが負の場合(plusとminusで尺取り法)
        j = p-1
        for i in range(m)[::-1]:
            while j >= 0:
                if minus[i]*plus[j] <= x:
                    j -= 1
                else:
                    break
            cnt += p - j - 1
    else: # xが正の場合(x>=0)
        #正の数同士で尺取り法
        j = p-1
        for i in range(p):
            while j >= 0:
                if plus[i]*plus[j] > x:
                    j -= 1
                else:
                    break
            cnt += max(0,j - i)
        #負の数同士で尺取り法
        j = 0
        for i in range(m)[::-1]:
            while j < m:
                if minus[i]*minus[j] > x:
                    j += 1
                else:
                    break
            cnt += max(0,i - j)
        # 0x何かの場合 + 0x0の場合 + 負の数x正の数の場合
        cnt += (m+p)*zero + zero*(zero-1)//2 + m*p
    #k個以上あるならtrue
    return cnt >= k
        
n,k = LI()
a = LI()
a.sort()
minus = [x for x in a if x < 0]
plus = [x for x in a if x > 0]
m = len(minus)
p = len(plus)
zero = bl(a,1) - br(a,-1)
ok = 10**18
ng = -10**18-1
while ok-ng > 1:
    mid = (ok+ng)//2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)


    
