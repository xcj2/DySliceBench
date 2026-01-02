import sys
from itertools import product,combinations
from functools import reduce,lru_cache
import heapq

def vfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:f(*x,**kwargs),*lst))

def rvfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:rvfunc(f)(*x,**kwargs) if all(vfunc(lambda y:isinstance(y,list))(x)) else f(*x,**kwargs),*lst))

def reader():return vfunc(lambda l:l.split())(sys.stdin.readlines())

x,k,d=vfunc(int)(reader()[0])

x=abs(x)
if d*k<x:print(x-d*k)
else:
    k0 = int(x/d)+1
    x0 = abs(x-d*k0)
    print(x0 if (k-k0)%2==0 else (d-x0))
