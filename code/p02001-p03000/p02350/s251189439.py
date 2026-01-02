import sys
input=sys.stdin.readline

def gindex(l,r):
    L,R=l+N0,r+N0
    lm=L//(L&-L)>>1
    rm=R//(R&-R)>>1
    while L<R:
        if R<=rm:
            yield R
        if L<=lm:
            yield L
        L>>=1
        R>>=1
    while L:
        yield L
        L>>=1
def propagates(*ids):
    for i in reversed(ids):
        v=lazy[i-1]
        if v==None:
            continue
        lazy[2*i-1]=v
        lazy[2*i]=v
        data[2*i-1]=v
        data[2*i]=v
        lazy[i-1]=None
def update(l,r,x):#1-index [s,t)
    L,R=N0+l,N0+r
    *ids,=gindex(l,r)
    propagates(*ids)
    while L<R:#上から
        if R&1:
            R-=1
            lazy[R-1]=x
            data[R-1]=x
        if L&1:
            lazy[L-1]=x
            data[L-1]=x
            L+=1
        L>>=1
        R>>=1
    for i in ids:#下から
        data[i-1]=min(data[2*i-1],data[2*i])
def query(l,r):
    propagates(*gindex(l,r))
    L,R=N0+l,N0+r
    s=INF
    while L<R:
        if R&1:
            R-=1
            s=min(s,data[R-1])
        if L&1:
            s=min(s,data[L-1])
            L+=1
        L>>=1
        R>>=1
    return s
n,q=map(int,input().split())

LV=n.bit_length()
N0=2**LV
INF=2**40
data=[2**31-1]*2*N0
lazy=[None]*2*N0
for i in range(q):
    l=list(map(int,input().split()))
    if l[0]==0:
        s,t,x=l[1:]
        update(s,t+1,x)
    else:
        s,t=l[1:]
        print(query(s,t+1))

