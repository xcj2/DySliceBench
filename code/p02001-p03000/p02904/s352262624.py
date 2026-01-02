from collections import deque

def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]

n,k=MI()
a=LI()

def slidmin(a,k):
    n=len(a)
    b=[0 for i in range(n-k+1)]
    q=deque()
    for i in range(k):
        while q and a[q[-1]]>=a[i]:
            q.pop()
        q.append(i)
    b[0]=a[q[0]]
    s=len(q)
    for i in range(k,n):
        while q and a[q[-1]]>=a[i]:
            q.pop()
            s-=1
        q.append(i)
        s+=1
        if q[0]<=i-k:
            q.popleft()
            s-=1
        b[i-k+1]=a[q[0]]
    return b

m=slidmin(a,k)
M=[-i for i in slidmin([-i for i in a],k)]
ans=1
p=-1
c=0
for i in range(k):
    if p<a[i]:
        c+=1
    else:
        c=1
    p=a[i]
fl=True if c==k else False

for i in range(n-k):
    if p<a[i+k]:
        c+=1
    else:
        c=1
    p=a[i+k]
    
    inc=1
    if c==k:
        if fl:
            inc=0
        fl=True
    if a[i]==m[i] and a[i+k]==M[i+1]:
        inc=0
    ans+=inc
print(ans)
