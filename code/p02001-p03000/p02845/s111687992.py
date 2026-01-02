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
    a=inpl()
    ans=1
    num=[0,0,0]
    for i in range(n):
        cnt=0
        index=0
        for j in range(3):
            if num[j]==a[i]:
                cnt+=1
                index=j
        num[index]+=1
        if cnt==1:
            ans=ans%mod
            continue
        elif cnt==2:
            ans=(ans*2)%mod
        elif cnt==3:
            ans=(ans*3)%mod
        else:
            print(0)
            return
    print(ans%mod)

if __name__ == "__main__":
    main()