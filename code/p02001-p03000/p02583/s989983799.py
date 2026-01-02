import sys
from itertools import product,combinations
from functools import reduce,lru_cache
import heapq

def vfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:f(*x,**kwargs),*lst))

def rvfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:rvfunc(f)(*x,**kwargs) if all(vfunc(lambda y:isinstance(y,list))(x)) else f(*x,**kwargs),*lst))

def reader():return vfunc(lambda l:l.split())(sys.stdin.readlines())

s=reader()
n,l=int(s[0][0]),vfunc(int)(s[1])
print(sum(vfunc(lambda args:((args[0]+args[1])>args[2]) and ((args[0]+args[2])>args[1]) and ((args[1]+args[2])>args[0]))(list(filter(lambda a:a[0]!=a[1] and a[2]!=a[1] and a[0]!=a[2],combinations(l,3))))))
