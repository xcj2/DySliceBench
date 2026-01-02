def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
#import numpy as np
import sys
import math
import collections
par = []
def init(n):
    for i in range(n):
        par.append(i)

def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def same(x,y):
    if root(x) == root(y):
        return True
    else:
        return False

def unite(x,y):
    x = root(x)
    y = root(y)
    if x==y:
        return
    par[y] = x
n,m = L()
ab = NL(m)
init(n)
#print(ab)
#print(par)
for a,b in ab:
    unite(a-1,b-1)
    #print(par)

for i in range(len(par)):
    root(i)
#print(par)
count = collections.Counter(par)
print(len(count)-1)