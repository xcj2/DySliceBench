# -*- coding: utf-8 -*-
import numpy as np
from math import factorial
from itertools import permutations

def cmb_fnct(MOD):
    #MOD:素数
    fact_mod = [1,1]
    inv_mod = [0,1]
    inv_fact_mod = [1,1]
    i = len(fact_mod)
    i_ = len(inv_fact_mod)

    def cmb(n,r):
        nonlocal i, i_
        r = min(r, n-r)
        if r<0: 
            return 0
        if r==0:
            return 1
        if r==1: 
            return n%MOD

        while n >= i:
            fact_mod[i:i] = [(fact_mod[i-1]*i)%MOD]
            i += 1

        while n-r >= i_:
            inv_mod[i_:i_] = [(-inv_mod[MOD%i_]*(MOD//i_))%MOD]
            inv_fact_mod[i_:i_] = [(inv_fact_mod[i_-1]*inv_mod[i_])%MOD]
            i_ += 1

        return fact_mod[n] * inv_fact_mod[r] * inv_fact_mod[n-r] % MOD
    return cmb

def solve():
    X, Y = map(int, input().split())
    a = -(X-2*Y)/3
    b = -(-2*X+Y)/3
    if a == int(a) and b == int(b):
        a = int(a)
        b = int(b)
    else:
        return '0'
    cmb = cmb_fnct(10**9+7)

    return str(cmb(a+b,a))

if __name__ == '__main__':
    print(solve())
