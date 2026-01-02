#!/usr/bin/env python

import sys

class bigint:
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
        return bigint(self.n+other.n,self.mod)
    #
    def __iadd__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        self.n = (self.n + other.n) % self.mod
        return self
    #
    def __sub__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return bigint(self.n-other.n,self.mod)
    #
    def __isub__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        self.n = (self.n - other.n) % self.mod
    #
    def __mul__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return bigint(self.n*other.n,self.mod)
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
        elif other==0: return bigint(1,self.mod)
        elif other==1: return self
        elif other%2==0:
            tmp= self ** (other//2)
            return bigint( ( tmp.n**2 ) % self.mod,self.mod )
        else:
            tmp= self ** (other//2)
            return bigint( ( tmp.n**2 * self.n ) % self.mod,self.mod )
    #
    def __truediv__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return self * ( other ** (other.mod-2) )
    #
    def __itruediv__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        self*= ( other ** (other.mod-2) )
        return self
#..................................................
fact= list()
def pair(maru,bou):
    global fact
    a= fact[maru+bou]
    b= fact[maru] * fact[bou]
    return a/b
#..................................................
n,k = [ int(x) for x in sys.stdin.readline().split() ]
#
r = n-k
fact.append( bigint(1) )
for i in range(1,n+1): fact.append( fact[i-1]*bigint(i) )

for block in range(1,k+1):
    # blue
    bp = k - block
    tmp = pair(bp,block-1)
    # red
    rp = r - ( block - 1 )
    if rp>=0: tmp *= pair(rp,block)
    else: tmp= 0
    #
    print( tmp )
