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


def main():
    d,g=inpm()
    p,c,t=[],[],[]
    ans=10**5
    for i in range(d):
        x,y=inpm()
        p.append(x)
        c.append(y)
        t.append(x*(i+1)*100+y)
    for num in range(1,d+1):
        for groop in combinations(range(d),num):
            total = 0
            member = 0
            for e in groop:
                total += t[e]
                member += p[e]
            if total < g:
                continue
            notgroup = []
            for i in range(d):
                if i not in groop:
                    notgroup.append(i)
            max_e=-1
            if len(notgroup)>0:
                max_e = max(notgroup)
            if max_e == d-1 or max_e==-1:
                pre_ans = 0
                for i in groop:
                    pre_ans += p[i]
                ans = min(ans,pre_ans)
            if max_e!=d-1:
                for way in range(max_e+1,d):
                    if total - c[way] - (way+1)*100 <g:
                        continue
                    diff = total - g - c[way] - (way+1)*100
                    pre_ans = member - 1 - min(p[way]-1,diff//((way+1)*100))
                    ans = min(ans,pre_ans)
    print(ans)

if __name__ == "__main__":
    main()