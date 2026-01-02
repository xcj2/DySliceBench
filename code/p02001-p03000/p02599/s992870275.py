'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7
alp = "abcdefghijklmnopqrstuvwxyz"

def Mo(n,q,c,qi,base):
    ans = [0]*q
    ln = [-1]*(n+1)

    #BITの構成
    BIT = [0]*(n+1)
    def BIT_query(idx):
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx&(-idx)
        return res_sum
    def BIT_update(idx,x):
        while idx <= n:
            BIT[idx] += x
            idx += idx&(-idx)
        return

    #Rが小さい方から見ていく,BITによる累積和の処理を含む
    pr = 0
    for ist in qi:
        i = ist%(base)
        l = (ist//(base))%(base)
        r = ist//(base)**2
        for j in range(pr,r):
            cj = c[j]
            ij = ln[cj]
            if ij != -1:
                BIT_update(ij,-1)
            ln[cj] = j+1
            BIT_update(j+1,1)
        pr = r
        ans[i] = BIT_query(r)-BIT_query(l-1)
    return ans

def main():
    n,q = map(int,ipt().split())
    c = [int(i) for i in ipt().split()]
    qi = []
    base = 10**6+1
    for i in range(q):
        l,r = map(int,ipt().split())
        qi.append(r*(base**2)+l*base+i)
    qi.sort()

    ans = Mo(n,q,c,qi,10**6+1)

    for i in ans:
        print(i)

    return None

if __name__ == '__main__':

    main()
