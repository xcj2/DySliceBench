from operator import itemgetter
from heapq import heappush,heappop
N = int(input())
table=[]
for i in range(N):
    a,b = map(int,input().split())
    table.append([a,b,i])
A = sorted(table,key=itemgetter(0))
B = sorted(table,key=itemgetter(1))

graph=[]
for k in range(N):#距離、点
    graph.append([min(abs(A[k][0]-A[k-1][0]),abs( A[k][1]-A[k-1][1])),A[k][2],A[k-1][2]])
for k in range(N):
    graph.append([min(abs(B[k][0]-B[k-1][0]),abs( B[k][1]-B[k-1][1])),B[k][2],B[k-1][2]])

class Unionfindtree:
    def __init__(self,number):
        self.par = [i for i in range(number)]
        self.rank = [0]*(number)

    def find(self,x):#親を探す xの親を示す
        if self.par[x] ==x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self,x,y):#x,yを繋げる
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 
        if self.rank[px]<self.rank[py]:
            self.par[px]=py
        else:
            self.par[py]=px
        if self.rank[px]==self.rank[py]:
            self.rank[px] +=1
    
    def connect(self,x,y):#親が同じかみる
        return self.find(x)==self.find(y)
#クラスカル法
kei = Unionfindtree(N)
graph.sort()
dist =0
for d,i,j in graph:
    if not kei.connect(i,j):
        kei.union(i,j)
        dist +=d
print(dist)