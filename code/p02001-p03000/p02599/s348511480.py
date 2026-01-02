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

No=2**19
BIT=[0]*(No+1)
def addbit(i,x):
    while i<=No:
        BIT[i]+=x
        i+= i&-i
def getsum(i):
    s=0
    while i:
        s+=BIT[i]
        i-= i&-i
    return s
def sumbit(l,r):
    return getsum(r)-getsum(l-1)

j=1
for l,r,i in Q:
    while j<=r:
        t=c[j]
        if lastapp[t]:
            addbit(lastapp[t],-1)
        addbit(j,1)
        lastapp[t]=j
        j+=1
    ans[i]=sumbit(l,r)
print(*ans, sep = "\n")