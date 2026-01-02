n,m,k=map(int,input().split())
par=[-1]*n

# this par & rank are initialized lists
def find(x):
    global par
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
        
def unite(x,y):
    x,y=find(x),find(y)
    global par
    if x==y:return False
    else:
        if par[x]>par[y]:x,y=y,x
        par[x]+=par[y]
        par[y]=x
        return True

def size(x):
    return -par[find(x)]
def same(x,y):
    return find(x)==find(y)
from sys import stdin 
input=stdin.readline
friend=[0]*n
for i in range(m):
    a,s=map(int,input().split())
    a-=1;s-=1
    unite(a,s)
    friend[a]+=1
    friend[s]+=1
anti=[set() for i in range(n)]
for i in range(k):
    a,b=map(int,input().split())
    a-=1;b-=1
    anti[a].add(b)
    anti[b].add(a)

print(*[size(i)-1-sum(same(i,b) for b in anti[i])-friend[i] for i in range(n)],sep=" ")
