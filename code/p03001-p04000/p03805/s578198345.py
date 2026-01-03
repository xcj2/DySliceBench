from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
# import numpy as np
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
    n,m=inpm()
    g=[[] for _ in range(n)]
    for _ in range(m):
        a,b=inpm()
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    ans = 0
    for root in permutations(range(1,n)):
        if root[0] not in g[0]:
            continue
        key=0
        for i in range(n-2):
            if root[i] not in g[root[i+1]]:
                key=1
        if key==0:
            ans+=1
    print(ans)
        

if __name__ == "__main__":
    main()