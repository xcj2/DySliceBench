# from collections import Counter,defaultdict,deque
import sys
# import bisect
# import math
# import itertools
# import string
# import queue
# import copy
# import numpy as np
# import scipy
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# mod = 10**9+7

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
    n,m=inpm()
    s=list(input())
    s.reverse()
    s=tuple(s)
    ans = []
    now = 0
    while True:
        key = 0
        for go in range(m,0,-1):
            if now+go>=n:
                x=n-now
                ans.append(str(x))
                ans.reverse()
                print(' '.join(ans))
                return
            elif s[now + go]=='0':
                key = 1
                now+=go
                ans.append(str(go))
                break
        if key == 0:
            print(-1)
            return

if __name__ == "__main__":
    main()