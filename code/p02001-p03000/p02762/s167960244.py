n,m,k= map(int,input().split())
par = [-1]*n
def findsize(x):
    temp = par[x]
    if temp<0:return -1*temp
    else:return findsize(temp)
def find(x):
    if par[x]<0:return x
    else:
        par[x]=find(par[x])
        return par[x]
def unite(x,y):
    px,py=find(x),find(y)
    if px==py:return False
    else:
        if px<py:px,py=py,px
        par[px]+=par[py]
        par[py]=px
        return True
fl = []
for i in range(m):
    a,b= map(int,input().split())
    unite(a-1,b-1)
    fl.append((a-1,b-1))
bl = []
for i in range(k):
    c,d= map(int,input().split())
    bl.append((c-1,d-1))
points=[0]*n
for i in range(n):points[i]=findsize(find(i))-1
for i in range(m):
    (a1,b1)=fl[i]
    points[a1]-=1
    points[b1]-=1
for i in range(k):
    (c1,d1)=bl[i]
    if find(c1)==find(d1):
        points[c1]-=1
        points[d1]-=1
print(*points)