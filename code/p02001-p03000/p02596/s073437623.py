#from functools import lru_cache
import sys
from itertools import product
from itertools import combinations
from functools import reduce

def vfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:f(*x,**kwargs),*lst))

def rvfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:rvfunc(f)(*x,**kwargs) if all(vfunc(lambda y:isinstance(y,list))(x)) else f(*x,**kwargs),*lst))

def reader():return vfunc(lambda l:l.split())(sys.stdin.readlines())

k=int(input())
t=0
m=7%k
md=7%k
for i in range(k+1):
    if m==0:break
    else:
        md=(md*10)%k
        m=(m+md)%k
if i==k: i=-2
print(i+1)
