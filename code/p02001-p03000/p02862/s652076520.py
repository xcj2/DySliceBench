#!/usr/bin/env python
import sys
from math import modf

class Bigint:
    def __init__(self,n,mod=10**9+7):
        self.n = n % mod
        self.mod = mod
        return
    #
    def __str__(self):
        return str(self.n)
    #
    def __add__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return Bigint(self.n+other.n,self.mod)
    #
    def __iadd__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        self.n = (self.n + other.n) % self.mod
        return self
    #
    def __sub__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return Bigint(self.n-other.n,self.mod)
    #
    def __isub__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        self.n = (self.n - other.n) % self.mod
    #
    def __mul__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return Bigint(self.n*other.n,self.mod)
    #
    def __imul__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        self.n = ( self.n * other.n ) % self.mod
        return self
    #
    def __pow__(self,other):
        assert type(other)==int, "power should be integer"
        #
        if other<0: return self ** ( other % ( self.mod-1 ) )
        ret = Bigint(1,self.mod)
        now = Bigint(self.n,self.mod)
        while other>0:
            if other%2==0: pass
            else: ret *= now
            other//=2
            now*=now
        return ret
    #
    def __truediv__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return self * ( other ** (other.mod-2) )
    #
    def __itruediv__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        self*= ( other ** (other.mod-2) )
        return self


def _ia(): return [ int(x) for x in sys.stdin.readline().strip().split() ]

def main():
    x,y = _ia()

    b = (2*x - y)/3
    if b.is_integer():
        b = int("{:.0f}".format(b))
        if b<0: return 0
    else:
        return 0

    a = x - 2*b
    if a<0: return 0
    n = a + b
    m = min(a,b)
    ans = Bigint(1)
    for i in range(m,0,-1):
        ans *= Bigint(n)
        ans /= Bigint(i)
        n -= 1
    #
    return ans
#
if __name__=="__main__":
    print(main())
