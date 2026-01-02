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
    n,m = inpm()
    dic = defaultdict(int)
    x = 0
    y = 0
    for _ in range(m):
        ps = inpls()
        ps[0] = int(ps[0])
        if ps[1] == 'WA':
            dic[ps[0]] += 1
        elif ps[1] == 'AC' and dic[ps[0]]<10**6:
            x += 1
            y += dic[ps[0]]
            dic[ps[0]]= 10**6
    print(x,y)



if __name__ == "__main__":
    main()