def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
import sys
sys.setrecursionlimit(10**6)
n=N()
p=L()
size=(n+1)**2+1
ans=[0]*size
for i in range(1,n+1):
    for j in range(1,n+1):
        k=i*(n+1)+j
        ans[k]=min(i-1,j-1,n-i,n-j)
c=[1]*size
di=[-1,1,n+1,-n-1]
def f(k,i):
    if k+i>=size:
        return
    if ans[k]+c[k]<ans[k+i]:
        ans[k+i]-=1
        q.append(k+i)
t=0
for i in p:
    y=i%n
    if y==0:
        y=n
    x=(i+n-1)//n
    k=x*(n+1)+y
    c[k]=0
    t+=ans[k]
    q=[k]
    while q:
        k=q.pop()
        f(k,1)
        f(k,-1)
        f(k,n+1)
        f(k,-n-1)
print(t)