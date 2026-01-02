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

def main():
    n,q = map(int,ipt().split())
#    n = 5*10**5
#    q = 5*10**5
#    c = [int(i)+1 for i in range(n)]
    c = [int(i) for i in ipt().split()]
    qi = []
    for i in range(q):
        l,r = map(int,ipt().split())
        qi.append(r*((10**6+1)**2)+l*(10**6+1)+i)

    qi.sort()

    ans = [0]*q
    ln = [-1]*(n+1)
    bq_al = [0]*(n+1)

    #Bit_Indexed_Tree
    #A1 ... AnのBIT(1-indexed)
    BIT = [0]*(n+1)

    #A1 ~ Aiまでの和 O(logN)
    def BIT_query(idx):
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def BIT_update(idx,x):
        while idx <= n:
            BIT[idx] += x
            idx += idx&(-idx)
        return

    pr = 0
    for ist in qi:
        i = ist%(10**6+1)
        l = (ist//(10**6+1))%(10**6+1)
        r = ist//(10**6+1)**2
        for j in range(pr,r):
            cj = c[j]
            ij = ln[cj]
            if ij != -1:
                BIT_update(ij,-1)
            ln[cj] = j+1
            BIT_update(j+1,1)
        pr = r

        ans[i] = BIT_query(r)-BIT_query(l-1)


    for i in ans:
        print(i)

    return None

if __name__ == '__main__':

    main()
