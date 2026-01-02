import math,sys,bisect,heapq
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
sys.setrecursionlimit(200000000)
input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
ilele = lambda: map(int,input().split())
alele = lambda: list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
#def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])


G = defaultdict(list)
first = 1 #  if node starts from 1

def addEdge(a,b):
    G[a].append(b)
	
def DFSutil(node,vis,size):
    vis[node] = True
    for child in G.get(node,[]):
        if vis[child] ==  False:
            DFSutil(child,vis,size)
        size[node] = max(size[node],1 + size[child])
    
def findsubtree(first,N):
    vis = [False] * (N+1)
    size = [0]* (N+1)
    for i in range(1,N+1):
        if vis[i] == False:
            DFSutil(i,vis,size)
    return max(size)
        
N,M = ilele()
G = defaultdict(list)
for i in range(M):
    u,v =ilele()
    addEdge(u,v)
print(findsubtree(first,N)) #returns size of each node in the array