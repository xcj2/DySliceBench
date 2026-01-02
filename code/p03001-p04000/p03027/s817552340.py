# -*- coding: utf-8 -*-
def PoAP_fnct(MOD):
    #MOD:素数
    fact_mod = [1,1]
    inv_mod = [0,1]
    inv_fact_mod = [1,1]
    i = len(fact_mod)
    i_ = len(inv_fact_mod)

    def PoAP(x,d,n):
        nonlocal i, i_
        if d == 0:
            return pow(x,n%(MOD-1),MOD)

        while d >= i_:
            inv_mod[i_:i_] = [(-inv_mod[MOD%i_]*(MOD//i_))%MOD]
            inv_fact_mod[i_:i_] = [(inv_fact_mod[i_-1]*inv_mod[i_])%MOD]
            i_ += 1

        j = (-x*inv_mod[d])%MOD
        if j < n:
            return 0

        x = (x*inv_mod[d])%MOD

        while (x+n-1)%MOD >= i:
            fact_mod[i:i] = [(fact_mod[i-1]*i)%MOD]
            i += 1

        while x-1 >= i_:
            inv_mod[i_:i_] = [(-inv_mod[MOD%i_]*(MOD//i_))%MOD]
            inv_fact_mod[i_:i_] = [(inv_fact_mod[i_-1]*inv_mod[i_])%MOD]
            i_ += 1

        return fact_mod[(x+n-1)%MOD] * inv_fact_mod[x-1] * pow(d,n%(MOD-1),MOD) % MOD
    return PoAP

def solve():
    Q = int(input())
    PoAP = PoAP_fnct(1000003)
    res = '\n'.join([str(PoAP(*map(int, input().split()))) for _ in range(Q)])
    return str(res)

if __name__ == '__main__':
    print(solve())

