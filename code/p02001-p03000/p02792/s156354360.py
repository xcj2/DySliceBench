#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def foo(n,x,y):
    l = len(n)
    sm = 0
    if x==y and (l>1 or n[0]>=x):
        sm = 1
    if l==1:
        return sm
    for i in range(2,l):
        sm += 10**(i-2)
    if x==n[-1]:
        sm += bar(n[:-1],y)
    elif x<n[-1]:
        sm += 10**(l-2)
    #ddprint(f"foo {n=} {x=} {y=} {sm=}")
    return sm

def bar(n,y):
    l = len(n)
    if l==1:
        return 1 if n[0]>=y else 0
    sm = (n[-1])*10**(l-2) + bar(n[:-1],y)
    return sm

nn = inn()
nnn = nn
n = []
while nn>0:
    n.append(nn%10)
    nn //= 10
sm = 0
for a in range(1,nnn+1):
    y = a%10
    if y==0:
        continue
    aa = a
    while aa>0:
        x = aa
        aa //= 10
    sm += foo(n,y,x)
print(sm)
