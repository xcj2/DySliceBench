#from functools import lru_cache
import sys
from itertools import product,combinations
from functools import reduce,lru_cache
import heapq
from math import ceil
def vfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:f(*x,**kwargs),*lst))

def list_t(l): return vfunc(lambda *args:args)(*l)

def rvfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:rvfunc(f)(*x,**kwargs) if all(vfunc(lambda y:isinstance(y,list))(x)) else f(*x,**kwargs),*lst))

def reader():return vfunc(lambda l:l.split())(sys.stdin.readlines())

n,x,t=vfunc(int)(reader()[0])
print((ceil(n/x))*t)