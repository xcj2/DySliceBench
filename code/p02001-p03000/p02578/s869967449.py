#from functools import lru_cache
import sys
from itertools import product,combinations
from functools import reduce,lru_cache
import heapq

def vfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:f(*x,**kwargs),*lst))

def list_t(l): return vfunc(lambda *args:args)(*l)

def rvfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:rvfunc(f)(*x,**kwargs) if all(vfunc(lambda y:isinstance(y,list))(x)) else f(*x,**kwargs),*lst))

def reader():return vfunc(lambda l:l.split())(sys.stdin.readlines())

n,a = rvfunc(int)(reader())
tmax=0
f=0
for i in range(n[0]):
    ai=a[i]
    if a[i]>tmax:tmax=a[i]
    f+=tmax-a[i]
print(f)