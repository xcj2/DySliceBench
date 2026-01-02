#from functools import lru_cache
import sys
import math
def vfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:f(*x,**kwargs),*lst))
def rvfunc(f): return lambda *lst, **kwargs: list(map(lambda *x:rvfunc(f)(*x,**kwargs) if all(vfunc(lambda y:isinstance(y,list))(x)) else f(*x,**kwargs),*lst))

def reader():return vfunc(lambda l:l.split())(sys.stdin.readlines())
sys.setrecursionlimit(100000)
ls = rvfunc(int)(reader())
n,k=ls[0]
a=ls[1]

def reqk(l):
    return sum(vfunc(lambda aa:math.ceil(aa/float(l))-1)(a))
def binary_search(imin=None,imax=None):
    if [imin,imax]==[None]*2: imin,imax=1,10**9+1
    if (imax < imin):
        return imin
    else:
        imid = int(imin + (imax - imin) / 2)
        if (reqk(imid)<=k):return binary_search(imin, imid - 1)
        elif (reqk(imid)>k):return binary_search(imid + 1, imax)
print(binary_search() if k!=0 else max(a))
