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
    t1,t2=inpm()
    a1,a2=inpm()
    b1,b2=inpm()
    if t1*a1+t2*a2 == t1*b1+t2*b2:
        print('infinity')
        return
    if t1*a1+t2*a2 < t1*b1+t2*b2:
        a1,b1 = b1,a1
        a2,b2 = b2,a2
    x = t1*a1+t2*a2 - (t1*b1+t2*b2)
    y = t1*a1-b1*t1
    if y>=0:
        print(0)
        return
    y*=-1
    ans=2*((y//x)+1)-1
    if y%x==0:
        ans-=1
    print(ans)
    

if __name__ == "__main__":
    main()