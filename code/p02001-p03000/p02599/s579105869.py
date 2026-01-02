import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
n,q=NM()
c=[0]+L()
Q=[L()+[i] for i in range(q)]
Q.sort(key=lambda x:x[1])
ans=[0]*(q)
lastapp=[0 for i in range(n+1)]

No=2
while No<=n:
    No*=2
tree=[0]*(2*No)

def update(k,x):
    k+=No-1
    tree[k]=x
    while k>0:
        k=(k-1)//2
        tree[k]=tree[k*2+1]+tree[k*2+2]

def add(k,x):
    k+=No-1
    while k>=0:
        tree[k]+=x
        k=(k-1)//2

def query(l,r):
    L=l+No-1
    R=r+No-1
    s=0
    while L<=R:
        if R&1:
            s+=tree[R]
            R-=2
        else:
            R-=1
        if L&1:
            L-=1
        else:
            s+=tree[L]
        L>>=1;R>>=1
    return s
j=1
for l,r,i in Q:
    while j<=r:
        t=c[j]
        add(lastapp[t],-1)
        add(j,1)
        lastapp[t]=j
        j+=1
    ans[i]=query(l,r)
for i in ans:
    print(i)