from collections import Counter
n,k,l=map(int,input().split())
#union-find
par1=[-1]*(n+1)
par2=[-1]*(n+1)

def find1(x):
    if par1[x]<0:
        return x
    else:
        par1[x]=find1(par1[x])
        return par1[x]
def find2(x):
    if par2[x]<0:
        return x
    else:
        par2[x]=find2(par2[x])
        return par2[x]
def size1(x):
    return -par1[find1(x)]
def size2(x):
    return -par2[find2(x)]
def unite1(x,y):
    if find1(x)==find1(y):
        return False
    else:
        if size1(x)<size1(y):
            x,y=y,x
        X=find1(x)
        Y=find1(y)
        par1[X]-=size1(Y)
        par1[Y]=X
        return True
def unite2(x,y):
    if find2(x)==find2(y):
        return False
    else:
        if size2(x)<size2(y):
            x,y=y,x
        X=find2(x)
        Y=find2(y)
        par2[X]-=size2(Y)
        par2[Y]=X
        return True
def is_same1(x,y):
    return find1(x)==find1(y)
def is_same2(x,y):
    return find2(x)==find2(y)

for _ in range(k):
    p,q=map(int,input().split())
    unite1(p,q)
for _ in range(l):
    r,s=map(int,input().split())
    unite2(r,s)
L=[]
for i in range(1,n+1):
    L.append((find1(i),find2(i)))
kazu=Counter(L)
ans=[0]*(n)
for i in range(n):
    ans[i]=kazu[L[i]]
print(*ans, sep=' ')