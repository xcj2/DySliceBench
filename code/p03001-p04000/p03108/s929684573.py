n,m=map(int,input().split())
ab=[]
l=[0 for i in range(n+1)]
for i in range(m):
    a=[int(j)-1 for j in input().split()]
    ab.append(a)

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

ans=[0 for i in range(m)]
ans[m-1]=n*(n-1)//2

for i in range(1,m):
    i=m-i
    ans[i-1]=ans[i]
    if root(ab[i][0])!=root(ab[i][1]):
        ans[i-1]-=size(ab[i][0])*size(ab[i][1])
        connect(ab[i][0],ab[i][1])

for i in range(m):
    print(ans[i])


