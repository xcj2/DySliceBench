import sys
sys.setrecursionlimit(10**7)

def modinv(a,m=10**9+7):
    if a==0: return 1
    b=m
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return lastx % m

def cur(p):
    for x in neighbor[p]:
        if x==par[p]: continue
        else:
            par[x]=p
            descend[p]+=cur(x)
    neighbor[p].remove(par[p])
    return descend[p]

def cur2(p):
    for x in neighbor[p]:
        ans[x]=ans[p]*descend[x]*modinv(n-descend[x])%mod
        cur2(x)

mod=10**9+7
n=int(input())
neighbor=[[]  for _ in range(n+1)]
descend=[1]*(n+1)
par=[0]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    neighbor[a].append(b)
    neighbor[b].append(a)
neighbor[1].append(0)
cur(1)

ans=[1]*(n+1)
ans1=1
for i in range(1,n+1):
    ans1=ans1*i*modinv(descend[i])%mod
ans[1]=ans1
cur2(1)
for i in range(1,n+1):
    print(ans[i])
