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
    return sorted([list(map(int, input().split())) for _ in range(n)])
def sortx(x,n,k):
    if k == 0:x.sort(key=lambda y:y[1,n])
    else:x.sort(reversed=True, key=lambda y:y[1,n])
def graph():
    n,m=inpm()
    g=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=inpm()
        a-=1
        b-=1
        g[a].append(b)
        g[b].append(a)
    return n,m,g
 
def main():
    n=inp()
    s=input()
    r,l=0,0
    ans=[]
    for i in range(n):
        if s[i]=='(':
            r+=1
        elif s[i]==')':
            if r==0:
                l+=1
            else:
                r-=1
    for i in range(l):
        ans.append('(')
    for i in range(n):
        ans.append(s[i])
    for i in range(r):
        ans.append(')')
    print(''.join(ans))


if __name__ == "__main__":
    main()