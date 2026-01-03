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

def main():
    n,a,b,c,d = inpm()
    if (c+d)+(n-1)*(c-d) <= 1 and a-(n-1)*d <= b and b <= a+(n-1)*d:
        print('YES')
        return
    for i in range(n):
        left = a - (n-1)*d + i*( (n-1)*(d-c) + (c+d)+(n-1)*(c-d) )
        right = left + (n-1)*(d-c)
        if left <= b and b <= right:
            print('YES')
            return
    print('NO')

if __name__ == "__main__":
    main()