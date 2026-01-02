import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input()) # n=1
def inpm(): return map(int,input().split()) # x=1,y=2
def inpl(): return list(map(int, input().split())) # a=[1,2,3,4,5,...,n]
def inpls(): return list(input().split())  # a=['1','2','3',...,'n']
def inplm(n): return list(int(input()) for _ in range(n)) # x=[] 複数行
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)] # [[2,2,2,2],[1,1,1,1],[3,3,3,3]] 
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)]) # [[1,1,1,1],[2,2,2,2],[3,3,3,3]] 
def graph():
    n=inp()
    g=[[] for _ in range(n)]
    for i in range(n):
        a = inp()
        a -= 1
        g[i].append(a)
        g[a].append(i)
    return n,g

def f(n):
    sumation = 0
    while n > 0:
        sumation += n%10
        n //= 10
    return sumation

def main():
    k = inp()
    a = inpl()
    a.reverse()
    x,y = 2,2
    for i in range(k):
        pair = a[i]
        if y < pair:
            print(-1)
            return
        if (y//pair)*pair < x:
            print(-1)
            return
        if pair >= x:
            x = pair
        elif x%pair != 0:
            s = x//pair + 1
            x = s*pair
        y = (y//pair+1) * pair - 1
        if y < x:
            print(-1)
            return
    print(x,y)
    
if __name__ == "__main__":
    main()