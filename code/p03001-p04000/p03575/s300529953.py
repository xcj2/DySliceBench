###==================================================
### import
#import bisect
#from collections import Counter, deque, defaultdict
#from copy import deepcopy
#from functools import reduce, lru_cache
#from heapq import heappush, heappop
#import itertools
#import math
#import string
import sys
### stdin
def input(): return sys.stdin.readline()
def iIn(): return int(input())
def iInM(): return map(int, input().split())
def iInM1(): return map(int1, input().split())
def iInLH(): return list(map(int, input().split()))
def iInLH1(): return list(map(int1, input().split()))
def iInLV(n): return [iIn() for _ in range(n)]
def iInLV1(n): return [iIn()-1 for _ in range(n)]
def iInLD(n): return [iInLH() for _ in range(n)]
def iInLD1(n): return [iInLH1() for _ in range(n)]
def sInLH(): return list(input().split())
def sInLV(n): return [input().rstrip('\n') for _ in range(n)]
def sInLD(n): return [sInLH() for _ in range(n)]
### stdout
def OutH(lst, deli=' '): print(deli.join(map(str, lst)))
def OutV(lst): print('\n'.join(map(str, lst)))
### setting
sys.setrecursionlimit(10 ** 6)
### utils
int1 = lambda x: int(x) - 1
### constants
INF = int(1e9)
MOD = 1000000007
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
###---------------------------------------------------

## begin library unionfind
## usage: uf = UnionFind()
## usage: r = uf.Find_Root(x)
## usage: uf.Unite(x, y)
## usage: bool = uf.isSameGroup(x, y)
## usage: n = uf.Count(x)
class UnionFind():

    def __init__(self, n):
        self.n = n # number of nodes
        # if root[x]<0 then x is root and it has |x| leafs
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    # find root of node x
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # path compression
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
    # unite two trees which has node x and node y
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # same tree
        if(x == y):
            return
        # different tree
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # if same rank (same depth)
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # return number of leafs
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

## end library unionfind

N, M = iInM()
AB = iInLD1(M)

## 枝を一つずつ選んで、それ以外を全部つなげてみて、非連結になるか見る
## 一つの森を作る計算量: MlogN
## それをM回繰り返すので、全体の計算量: M^2 logN = N^4 logN

ans = 0
for i in range(M):
    ## 選んだ枝以外で森を作る
    uf = UnionFind(N)
    for j in range(M):
        if j == i:
            continue
        uf.Unite(AB[j][0], AB[j][1])
    if uf.Count(0) != N:
        ans += 1
    
print(ans)


