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
    ans=n
    for t in range(min(5,n//46656)+1):
        x1 = n-t*46656
        for s in range(min(5,x1//7776)+1):
            x2=x1-7776*s
            for r in range(min(5,x2//1296)+1):
                x3=x2-1296*r
                for q in range(min(5,x3//216)+1):
                    x4=x3-216*q
                    for p in range(min(5,x4//36)+1):
                        x5=x4-36*p
                        for o in range(min(5,x5//6)+1):
                            x6=x5-6*o
                            n1=x6//59049
                            x6-=59049*n1
                            n2=x6//6561
                            x6-=6561*n2
                            n3=x6//729
                            x6-=729*n3
                            n4=x6//81
                            x6-=81*n4
                            n5=x6//9
                            x6-=9*n5
                            ans=min(ans,o+p+q+r+s+t+n1+n2+n3+n4+n5+x6)
    print(ans)

if __name__ == "__main__":
    main()