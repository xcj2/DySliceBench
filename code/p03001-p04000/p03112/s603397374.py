#119-D
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(input())
def S(): return input()
import bisect
a,b,q=IL()
s=[]
t=[]
for i in range(a):
    tmp=I()
    s.append(tmp)
for i in range(b):
    tmp=I()
    t.append(tmp)
inf=10**15
for i in range(q):
    rs,ls,rt,lt=inf,inf,inf,inf
    x=I()
    ts=bisect.bisect(s,x)
    tt=bisect.bisect(t,x)
    if ts!=0:
        ls=abs(x-s[ts-1])
    if tt!=0:
        lt=abs(x-t[tt-1])
    if ts!=a:
        rs=abs(s[ts]-x)
    if tt!=b:
        rt=abs(t[tt]-x)
    print(min(min(rs,lt)*2+max(rs,lt),min(rt,ls)*2+max(rt,ls),max(lt,ls),max(rt,rs)))