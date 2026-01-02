n,m=map(int,input().split())

#Union-Find
par=[-1 for i in range(n)]

def root(a):
    if par[a]<0:
        return a
    else:
        return root(par[a])

def size(a):
    return -par[root(a)]

def connect(a,b):
    a=root(a)
    b=root(b)
    if a==b:
        return False
    if size(a)<size(b):
        a,b=b,a
    par[a]+=par[b]
    par[b]=a
    return True

xyz=[]
for i in range(m):
    a=[int(j) for j in input().split()]
    xyz.append([a[0]-1,a[1]-1,a[2]%2])
    if root(a[0]-1)!=root(a[1]-1):
        connect(a[0]-1,a[1]-1)
ans=0
for i in range(n):
    if par[i]<0:
        ans+=1
print(ans)