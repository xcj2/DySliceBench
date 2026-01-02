import sys
input=sys.stdin.readline
from math import factorial
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:   #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True
def same(x,y):
    return find(x) == find(y)
def size(x):
    return -par[find(x)]

n,m=map(int,input().split())
par = [-1]*n
lst=[]
for i in range(m):
    a,b=map(int,input().split())
    lst.append([a-1,b-1])
lst.reverse()
anslst=[(factorial(n)//(2*factorial(n-2)))]
for i in range(m-1):
    a,b=lst[i]
    if same(a,b):
        anslst.append(anslst[-1])
    else:
        c=size(a)*size(b)
        anslst.append(anslst[-1]-c)
        union(a,b)
anslst.reverse()
for i in anslst:
    print(i)