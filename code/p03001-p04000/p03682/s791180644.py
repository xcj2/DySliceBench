import sys
read=sys.stdin.readline
def find(x):
    if(par[x]==x):
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if(a==b):
        return 0
    else:
        if rank[a]>rank[b]:
            par[b]=a
        else:
            par[a]=b
            if rank[a]==rank[b]:
                rank[b]+=1
def same(a,b):
    return find(a)==find(b)
def Kruskal(Edge,E):
    cost=0
    Edge.sort(key=lambda x:x[2])
    for i in range(E):
        f,t,c=Edge[i]
        if(not same(f,t)):
            union(f,t)
            cost+=c
    return cost

N=int(input())
par=[];p=[];dic={};rank=[]
for i in range(N):
    par.append(i)
    rank.append(0)
    p.append(tuple(map(int,read().split())))
    dic[p[i]]=i
xp=sorted(p,key=lambda x:x[0])
yp=sorted(p,key=lambda x:x[1])
Edge=[]
for i in range(N):
    if(i>0):
        Edge.append((dic[xp[i]],dic[xp[i-1]],abs(xp[i][0]-xp[i-1][0])))
    if(i<N-1):
        Edge.append((dic[xp[i]],dic[xp[i+1]],abs(xp[i][0]-xp[i+1][0])))
    if(i>0):
        Edge.append((dic[yp[i]],dic[yp[i-1]],abs(yp[i][1]-yp[i-1][1])))
    if(i<N-1):
        Edge.append((dic[yp[i]],dic[yp[i+1]],abs(yp[i][1]-yp[i+1][1])))
print(Kruskal(Edge,len(Edge)))