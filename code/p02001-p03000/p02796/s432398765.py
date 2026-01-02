from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
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
    n = inp()
    LR = []
    for _ in range(n):
        x,l = inpm()
        LR.append((x-l,x+l))
    LR.sort()
    ans = 1
    index = 1
    l,r = LR[0]
    while index < n:
        if LR[index][0] < r and l < LR[index][1]:
            r = min(r,LR[index][1])
            index += 1
        else:
            ans += 1
            [l,r] = LR[index]
            index += 1
    print(ans)

if __name__ == "__main__":
    main()