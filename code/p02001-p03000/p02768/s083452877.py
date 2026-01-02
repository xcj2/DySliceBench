#!/bin/bash
''':'
docker run --rm -it -v $(cd $(dirname $0) && pwd):/vo:ro pypy:3-2.4.0 \
   /bin/bash -c "pypy3 /vo/$(basename $0) < /vo/g.inp"
exit $?
'''
import sys

def _ia(): return [ int(x) for x in sys.stdin.readline().strip().split() ]

class Bigint:
    def __init__(self,n,mod=10**9+7):
        self.n = n % mod
        self.mod = mod
        return


    def __str__(self):
        return str(self.n)


    def __add__(self,other):
        ot = type(other)
        if ot==Bigint:
            return Bigint(self.n+other.n,self.mod)
        elif ot==int:
            return Bigint(self.n+other,self.mod)
        else:
            raise ValueError("Invalid type")


    def __iadd__(self,other):
        return self.__add__(other)


    def __sub__(self,other):
        ot = type(other)
        if ot==Bigint:
            o = other.n
        elif ot==int:
            o = other
        else:
            raise ValueError("Invalid type")
        #
        return Bigint(self.n - o, self.mod)


    def __isub__(self,other):
        return self.__sub__(other)


    def __mul__(self,other):
        ot = type(other)
        if ot==Bigint:
            return Bigint(self.n*other.n,self.mod)
        elif ot==int:
            return Bigint(self.n*other,self.mod)
        else:
            raise ValueError("Invalid type")


    def __imul__(self,other):
        return self.__mul__(other)


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


    def __truediv__(self,other):
        ot = type(other)
        if ot==Bigint:
            o = other
        elif ot==int:
            o = Bigint(other)
        else:
            raise ValueError("Invalid type")

        self *= ( o ** (o.mod-2) )
        return self


    def __itruediv__(self,other):
        return self.__truediv__(other)

def combination(n,k):
   kp = min(k,n-k)

   ne = Bigint(1)
   for i in range(n-kp+1, n+1): ne *= i
   de = Bigint(1)
   for i in range(1, kp+1): de *= i
   return ne / de

n, a, b = _ia()
ans = Bigint(2) ** n - 1
ans -= combination(n,a)
ans -= combination(n,b)
print(ans)