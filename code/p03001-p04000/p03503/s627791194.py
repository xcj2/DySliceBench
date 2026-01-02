from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
#import numpy as np
# import scipy
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
 
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return [list(map(int, input().split())) for _ in range(n)]

def main():
    n=inp()
    f=[]
    for _ in range(n):
        f.append(inpl())
    p=[]
    for _ in range(n):
        p.append(inpl())
    ans=-10**10
    for i in range(1,11):
        for j in combinations(range(10),i):
            do = [0 for _ in range(10)]
            for k in j:
                do[k]=1
            benefit = 0
            for l in range(n):
                s=0
                for u in range(10):
                    s+=f[l][u]*do[u]
                benefit += p[l][s]
            ans=max(ans,benefit)
    print(ans)

if __name__ == "__main__":
    main()