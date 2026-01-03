#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,w = map(int,input().split()) #n:頂点数　w:辺の数
edge=[]
d = [[float("inf")]*n for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(w):
    x,y,z = map(int,input().split())
    x-=1
    y-=1
    edge.append([x,y,z])
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
warshall_floyd(d)
#print(edge)
count=0
for x,y,z in edge:
    flag=True
    for i in range(n):
        for j in range(n):
            if d[i][j]==d[i][x]+z+d[y][j]:
                #print(i,x,y,j)
                flag=False
    if flag==True:
        count+=1
print(count)

#インデックスで与えられていることに注意
#ソース　https://juppy.hatenablog.com/entry/2018/11/01/蟻本_python_全点対最短経路法（ワーシャルフロイド法
