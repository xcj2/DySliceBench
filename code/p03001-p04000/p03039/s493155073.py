#!/usr/bin/env python

import sys
#from sympy import isprime

class bigint:
    primeset = set()
    def __init__(self,n,mod):
        if not mod in bigint.primeset:
            assert mod**2 < sys.maxsize, "modulo is too large"
            #assert isprime(mod), "modulo should be a prime number"
            bigint.primeset.add(mod)
        #
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
    def __sub__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return bigint(self.n-other.n,self.mod)
    #
    def __mul__(self,other):
        assert self.mod==other.mod, "modulos of the two not match"
        return bigint(self.n*other.n,self.mod)
    #
    def __pow__(self,other):
        assert type(other)==int, "power should be integer"
        #
        if other<0: return self ** ( other % ( self.mod-1 ) )
        elif other==0: return 1
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
#::::::::::::::::::::::::::::::::::::::::::::::::::
mod= 10**9 + 7

def combination(n,m):
    global mod
    assert type(n)==type(m)==int, "type error"
    #
    mm= min(m,n-m)
    if mm==0: return bigint(1,mod)
    elif mm>0:
        a = bigint(n,mod)
        b = bigint(1,mod)
        for i in range(1,mm):
            a = a * bigint(n-i,mod)
            b = b * bigint(i+1,mod)
        return a / b
    #
    raise ValueError
#
n,m,k = [ int(x) for x in sys.stdin.readline().split() ]
#
# const.
nn= n * n
mm= m * m
cc= combination(n*m-2,k-2)

# initialize
score=bigint(0,mod)

# scan over horizontal direction
for i in range(1,n):
    score= score + bigint(i * mm * (n-i),mod) * cc

# scan over vertical direction
for i in range(1,m):
    score= score + bigint(i * nn * (m-i),mod) * cc
#
print( score )
