import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
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
    n = inp()
    dp = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(n+1):
        s = str(i)
        dp[int(s[0])][int(s[-1])] += 1
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            ans += dp[i][j] * dp[j][i]
    print(ans)

if __name__ == "__main__":
    main()