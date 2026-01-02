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
    s=list(input())
    for i in range(len(s)):
        s[i]=int(s[i])
    dic1=defaultdict(int)
    dic2=defaultdict(int)
    cnt1=0
    cnt=[0 for _ in range(10)]
    for i in range(n-2):
        if dic1[s[i]]==0:
            dic1[s[i]]=1
        for j in range(10):
            if dic1[j]==1:
                if dic2[j*10+s[i+1]]==0:
                    cnt1+=1
                    dic2[j*10+s[i+1]]=1
        cnt[s[i+2]]=cnt1
    print(sum(cnt))



if __name__ == "__main__":
    main()