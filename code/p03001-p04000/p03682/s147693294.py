from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations,groupby
import sys
import bisect
import string
import math
import time
import random
def S_():
    return input()
def LS():
    return [i for i in input().split()]
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def NI(n):
    return [int(input()) for i in range(n)]
def NI_(n):
    return [int(input())-1 for i in range(n)]
def StoI():
    return [ord(i)-97 for i in input()]
def ItoS(nn):
    return chr(nn+97)
def LtoS(ls):
    return ''.join([chr(i+97) for i in ls])
def GI(V,E,Directed=False,index=0):
    org_inp=[]
    g=[[] for i in range(n)]
    for i in range(E):
        inp=LI()
        org_inp.append(inp)
        if index==0:
            inp[0]-=1
            inp[1]-=1
        if len(inp)==2:
            a,b=inp
            g[a].append(b)
            if not Directed:
                g[b].append(a)
        elif len(inp)==3:
            a,b,c=inp
            aa=(inp[0],inp[2])
            bb=(inp[1],inp[2])
            g[a].append(bb)
            if not Directed:
                g[b].append(aa)
    return g,org_inp
def bit_combination(k,n=2):
    rt=[]
    for tb in range(n**k):
        s=[tb//(n**bt)%n for bt in range(k)]
        rt+=[s]
    return rt
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()

def ran_input():
    import random
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

show_flg=False
show_flg=True

class UnionFind:
    def __init__(self, n):
        # 負  : 根であることを示す。絶対値はランクを示す
        # 非負: 根でないことを示す。値は親を示す
        self.table = [-1] * n
 
    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            # 経路の圧縮
            self.table[x] = self._root(self.table[x])
            return self.table[x]
 
    def find(self, x, y):
        return self._root(x) == self._root(y)
 
    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        # ランクの取得
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2
    
    def __str__(self):
        rt=[i if j<0 else j for i,j in enumerate(self.table)]
        return str(rt)
        
def dijkstra(edge,st):
    # edge=[[(v_to,dist_to_v),...],[],...]
    # initialize: def: d=dist(st,i), prev=[previous vertex in minimum path], q[]
    n=len(edge)
    d=[(0 if st==i else inf) for i in range(n)]
    prev=[0]*n
    q=[(j,i) for i,j in enumerate(d)]
    heapify(q)
    
    # calc
    while q:
        dist,cur=heappop(q)
        for dst,dist in edge[cur]:
            alt=d[cur]+dist
            if alt<d[dst]:
                d[dst]=alt
                prev[dst]=cur
                heappush(q,(alt,dst))
    return d,prev

n=I()
p=[]
for i in range(n):
    x,y=LI()
    p.append((x,y,i))
    
X=sorted(p,key=lambda x:x[0])
Y=sorted(p,key=lambda x:x[1])

g=[[] for i in range(n)]
q=[]
for i in range(n-1):
    x0,y0,a=X[i]
    x1,y1,b=X[i+1]
    q.append((min(abs(x1-x0),abs(y1-y0)),a,b))
    
for i in range(n-1):
    x0,y0,a=Y[i]
    x1,y1,b=Y[i+1]
    q.append((min(abs(x1-x0),abs(y1-y0)),a,b))
    
uf=UnionFind(n)
q.sort(reverse=True,key=lambda x:x[0])

ans=0
e=n-1
while e:
    d,a,b=q.pop()
    if uf._root(a)!=uf._root(b):
        ans+=d
        uf.union(a,b)
        e-=1

print(ans)


