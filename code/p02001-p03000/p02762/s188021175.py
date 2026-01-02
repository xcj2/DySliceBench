import sys
sys.setrecursionlimit(10**6)

def root(x):
    if pair[x]<0:
        return x
    else:
        tmp=root(pair[x])
        pair[x]=tmp
        return tmp

def unite(x,y):
    x=root(x)
    y=root(y)
    if x==y:return False
    if pair[x]>pair[y]:
        x,y=y,x
    pair[x]+=pair[y]    
    pair[y]=x
    return True

def size(x):
    return -pair[root(x)]

icase=0
if icase==0:
    n,m,k=map(int,input().split())
    g=[[] for i in range(n)]
    x=[[] for i in range(n)]
    a=[0]*m
    b=[0]*m
    pair=[-1]*n
    for i in range(m):
        ai,bi=map(int,input().split())
        g[ai-1].append(bi-1)
        g[bi-1].append(ai-1)
        a[i]=ai-1
        b[i]=bi-1
        unite(a[i],b[i])
    for i in range(k):
        ci,di=map(int,input().split())
        x[ci-1].append(di-1)
        x[di-1].append(ci-1)

for i in range(n):
    ss=size(i)-1
    rooti=root(i)
    for gi in g[i]:
        if root(gi)==rooti:
            ss-=1
    for xi in x[i]:
        if root(xi)==rooti:
            ss-=1
    print(ss,end=" ")
print(" ")
    

