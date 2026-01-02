import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
input = sys.stdin.readline
    
icase=0
if icase==0:
    n,m=map(int,input().split())
    a=[0]*m
    b=[0]*m
    for i in range(m):
        ai,bi=map(int,input().split())
        a[i]=ai-1
        b[i]=bi-1

pair=[i for i in range(n)]

def root(x):
    if x==pair[x]:
        return x
    else:
        tmp=root(pair[x])
        pair[x]=tmp
        return tmp

def unite(x,y):
    x=root(x)
    y=root(y)
    if x==y:
        return
    elif x>y:
        pair[x]=y
    else:
        pair[y]=x

def q087():
    cc=[]
    c1=[1]*n
    c2=defaultdict(int)
    c2[1]=n
    c=n    
    for i in range(m-1):
        rta=root(a[m-i-1])
        rtb=root(b[m-i-1])
        if c1[rta]>=n or c1[rtb]>=n:
            cc.append(0)
            continue
        if rta<rtb:
            d2=c1[rta]
            d3=c1[rtb]
            c1[rta]+=c1[rtb]
            c1[rtb]=0
            d1=c1[rta]
#            pair[rtb]=rta
            unite(a[m-i-1],b[m-i-1])
        elif rta>rtb:
            d2=c1[rta]
            d3=c1[rtb]
            c1[rtb]+=c1[rta]
            c1[rta]=0
            d1=c1[rtb]
#            pair[rta]=rtb
            unite(a[m-i-1],b[m-i-1])
        else:
            cc.append(c)
            continue

        c2[d1]+=1    
        if c2[d2]>0:
            c2[d2]-=1
        if c2[d3]>0:
            c2[d3]-=1
        q=[]
        for c2k,c2v in c2.items():
            if c2v==0:
                q.append(c2k)
        while q:
            del c2[q.pop()]            
        c3=[]
        for c2k,c2v in c2.items():
            c3.append((c2k,c2k*c2v))

        c=0
        for i,c3i in enumerate(c3):
            c+=c3i[1]*(c3i[1]-c3i[0])//2
            for j,c3j in enumerate(c3[0:i]):
                c+=c3i[1]*c3j[1]
        cc.append(c)

    for i in range(m-2,-1,-1):
        print(cc[i])
    print(n*(n-1)//2)
#-------------------------------
q087()
#-------------------------------

