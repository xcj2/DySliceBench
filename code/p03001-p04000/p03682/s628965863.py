import sys
from heapq import*
from collections import*

input=sys.stdin.readline


p=defaultdict(lambda: -1)
class UNION_FIND(object):
    def __init__(self,n):
        
        self.parent=defaultdict(lambda: -1)

    def root(self,x):
        if type(self.parent[x])!=tuple:
            return x
        else:
            self.parent[x]=self.root(self.parent[x])
            return self.parent[x]
 
    def size(self,x):
        return -self.parent[self.root(x)]
    def union(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if x==y:
            return False
        if self.size(x)<self.size(y):
            x,y=y,x
        self.parent[x]+=self.parent[y]
        self.parent[y]=x
        return True
def compute_mst_kruskal(max_v, edges, flip):
    edges.sort(key=lambda x: x[2],reverse=flip)
    #print(edges)
    uf = UNION_FIND(max_v)
    mst = []
    for (a,b,c) in edges:
        if uf.root(a)!= uf.root(b):
            uf.union(a,b)
            mst.append(c)
    return mst


n = int(input())
points=[list(map(int,input().split()))for i in range(n)]

x=sorted(points,key=lambda x:x[0])
y=sorted(points,key=lambda x:x[1])
#print(x,y)


edges = []
for i in range(1,n):
    (a,b),(c,d)=x[i-1],x[i]
    (e,f),(g,h)=y[i-1],y[i]
    heappush(edges,((a,b),(c,d),abs(a-c)))
    heappush(edges,((e,f),(g,h),abs(f-h)))
#print(edges)
mst = compute_mst_kruskal(n, edges , 0) #0が最小化
print(sum(mst))
