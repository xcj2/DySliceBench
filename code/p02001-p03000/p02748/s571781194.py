import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

def main():
    A,B,M = inpm()
    a = inpl()
    b = inpl()
    ans = 10**20
    for _ in range(M):
        w,e,r = inpm()
        ans = min(ans,a[w-1]+b[e-1]-r)
    a.sort()
    ans = min(ans,min(a)+min(b))
    print(ans)
            
if __name__ == "__main__":
    main()