n,k,l=map(int,input().split())

#Union-Find
par=[-1 for i in range(n+1)]
def root(a):
    if par[a]<0:
        return a
    else:
        return root(par[a])
def f(a):
    if road[a]<0:
        return a
    else:
        return f(road[a])
def f2(a):
    if rail[a]<0:
        return a
    else:
        return f2(rail[a])
def size(a):
    return -par[root(a)]
def connect(a,b):
    a=root(a)
    b=root(b)
    if a==b:
        return False
    if size(a)<size(b):
        a,b=b,a
    par[a]+=par[b]
    par[b]=a
    return True

for i in range(k):
    a=[int(j) for j in input().split()]
    if root(a[0])!=root(a[1]):
        connect(a[0],a[1])
import copy
road=copy.deepcopy(par)

par=[-1 for i in range(n+1)]

for i in range(l):
    r,s=[int(j) for j in input().split()]
    if root(r)!=root(s):
        connect(r,s)
import copy
rail=copy.deepcopy(par)
l=[(f(i),f2(i)) for i in range(1,1+n)]
from collections import Counter
c=Counter(l)
print(*(c[i] for i in l))





