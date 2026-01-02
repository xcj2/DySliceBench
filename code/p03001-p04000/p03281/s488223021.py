#from functools import lru_cache
import sys
from itertools import product,combinations
from functools import reduce,lru_cache
import heapq

def vfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:f(*x,**kwargs),*lst))

def list_t(l): return vfunc(lambda *args:args)(*l)

def rvfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:rvfunc(f)(*x,**kwargs) if all(vfunc(lambda y:isinstance(y,list))(x)) else f(*x,**kwargs),*lst))

def reader():return vfunc(lambda l:l.split())(sys.stdin.readlines())

def factorization(n):
    out={}
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            out.update({i:0})
            while n%i==0:
                out[i]+=1
                n=int(n/i)
    if n != 1: out.update({n:1})
    return out

n=int(reader()[0][0])

dl = vfunc(lambda i:factorization(i))(range(1,n+1,2))
f = lambda d:reduce(lambda a,b:a*b,vfunc(lambda n:d[n]+1)(d)) if len(d)>1 else vfunc(lambda n:d[n]+1)(d)[0] if len(d)==1 else 0
s = vfunc(f)(dl)
#print(s)
print(len(list(filter(lambda a:a==8,s))))
