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
# input = sys.stdin.readline
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
    s=input()
    w=0
    for i in range(n):
        if s[i]=='.':
            w+=1
    b=n-w
    ans=n
    x=0
    y=w
    for i in range(n):
        ans=min(ans,x+y)
        if s[i]=='.':
            y-=1
        else:
            x+=1
        ans=min(ans,x+y)

    print(ans)

if __name__ == "__main__":
    main()