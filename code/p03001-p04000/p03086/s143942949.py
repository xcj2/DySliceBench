#from functools import lru_cache
import sys
from itertools import product,combinations,accumulate
from functools import reduce,lru_cache
import heapq

def vfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:f(*x,**kwargs),*lst))

def list_t(l): return vfunc(lambda *args:args)(*l)

def rvfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:rvfunc(f)(*x,**kwargs) if all(vfunc(lambda y:isinstance(y,list))(x)) else f(*x,**kwargs),*lst))

def reader():return vfunc(lambda l:l.split())(sys.stdin.readlines())

s = reader()[0][0]
score = [0]
for i in s:
    if i in 'ACGT':score.append(score[-1]+1)
    else:score.append(0)
print(max(score))