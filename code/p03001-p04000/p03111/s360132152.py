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
    ans=10**10
    n,a,b,c=inpm()
    l=inplm(n)
    for an in range(1,n-1):
        for use_a in combinations(range(n),an):
            tank = []
            for j in range(n):
                if j not in use_a:
                    tank.append(j)
            for bn in range(1,n-an):
                for use_b in combinations(tank,bn):
                    tank1=[]
                    for j in tank:
                        if j not in use_b:
                            tank1.append(j)
                    for cn in range(1,n-an-bn+1):
                        for use_c in combinations(tank1,cn):
                            a_pre=0
                            b_pre=0
                            c_pre=0
                            for i in use_a:
                                a_pre+=l[i]
                            for i in use_b:
                                b_pre+=l[i]
                            for i in use_c:
                                c_pre+=l[i]
                            cnt=0
                            cnt+= (len(use_a)+len(use_b)+len(use_c)-3)*10 + abs(a_pre-a)+abs(c_pre-c)+abs(b_pre-b)
                            if ans>cnt:
                                ans=cnt
                            
    print(ans) 

if __name__ == "__main__":
    main()