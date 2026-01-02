import sys
def input():return sys.stdin.readline()[:-1]
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
n=N()
l=L()
sx=0
for i in l[2:]:
    sx^=i
if sx>l[0]+l[1]:
    print(-1)
    quit()
if (l[0]+l[1]-sx)%2==1:
    print(-1)
    quit()
if sx^l[0]^l[1]==0:
    print(0)
    quit()
x=(l[0]+l[1]-sx)//2
y=x
if x&sx>0:
    print(-1)
    quit()
if x>l[0]:
    print(-1)
    quit()
for i in range(45,-1,-1):
    if sx>>i&1:
        if l[0]>=(x+(1<<i)):
            x+=(1<<i)
if x==0:
    print(-1)
    quit()
print(l[0]-x)