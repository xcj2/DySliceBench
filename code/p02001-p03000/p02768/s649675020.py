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

def combination(n,a,b):
    k = a
    ans = 1
    for i in range(n,n-k,-1):
        ans = ans*i%mod
    for i in range(1,k+1):
        ans = ans*pow(i,mod-2,mod)%mod
    ans1 = ans
    for i in range(n-k,n-b,-1):
        ans1 = ans1*i%mod
    for i in range(k+1,b+1):
        ans1 = ans1*pow(i,mod-2,mod)%mod
    return ans + ans1

def main():
    n,a,b = inpm()
    ans = pow(2,n,mod) - 1
    ans += mod
    ans -= combination(n,a,b)
    print(ans%mod)
    
if __name__ == "__main__":
    main()