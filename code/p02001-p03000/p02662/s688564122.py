import itertools
from collections import deque,defaultdict,Counter
from itertools import accumulate
import bisect
from heapq import heappop,heappush,heapify
import math
from copy import deepcopy
import queue
#import sympy as syp(素因数分解とか)
Mod = 1000000007
  
def sieve_of_eratosthenes(n):
    if not isinstance(n,int):
        raise TypeError("n is not int")
    if n<2:
        raise ValueError("n is not effective")
    prime = [1]*(n+1)
    for i in range(2,int(math.sqrt(n))+1):
        if prime[i] == 1:
            for j in range(2*i,n+1):
                if j%i == 0:
                    prime[j] = 0
    res = []
    for i in range(2,n+1):
        if prime[i] == 1:
            res.append(i)
    return res

 
class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
    
    def findroot(self,x):
        if x == self.parent[x]:
            return x
        else:
            y = self.parent[x]
            y = self.findroot(self.parent[x])
            return y
    
    def union(self,x,y):
        px = self.findroot(x)
        py = self.findroot(y)
        if px < py:
            self.parent[y] = px
        else:
            self.parent[px] = py
 
    def same_group_or_no(self,x,y):
        return self.findroot(x) == self.findroot(y)

def main():  #startline-------------------------------------------
    n, s = map(int,input().split())
    a = list(map(int, input().split()))
    dp = [[0] * (s + 1) for i in range(n + 1)]
    #dp[i][j]...最初のi個の数について。総和がjであるように選んでできる部分集合すべてについての集合の個数の総和
    dp[0][0] = 1
    for i in range(n):
        for j in range(s+1):
            dp[i + 1][j] += dp[i][j] * 2 % 998244353
            if j - a[i] >= 0:
                dp[i + 1][j] += dp[i][j - a[i]]
            dp[i + 1][j] %= 998244353
            
    print(dp[n][s])
if __name__ == "__main__":
    main() #endline===============================================