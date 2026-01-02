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
    return sorted([list(map(int, input().split())) for _ in range(n)])

    
def main():
    n=int(input())
    xyh=[]
    for _ in range(n):
        x,y,h=inpm()
        xyh.append([x,y,h])
    xyh.sort(key=lambda x: x[2], reverse=True)
    for xc in range(101):
        for yc in range(101):
            x=xyh[0][0]
            y=xyh[0][1]
            h=xyh[0][2]
            d=abs(xc-x)+abs(yc-y)
            H=h+d
            for i in range(1,n):
                x=xyh[i][0]
                y=xyh[i][1]
                h=xyh[i][2]
                d = abs(xc-x) + abs(yc-y)
                if h!=max(0,H-d):
                    break
                if i == n-1:
                    print(xc,yc,H)
                    return
if __name__ == "__main__":
    main()