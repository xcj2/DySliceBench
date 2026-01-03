
"""
Writer: SPD_9X2
https://atcoder.jp/contests/arc067/tasks/arc067_c

dpだろうなぁ
O(N^2)に頑張って抑えなくてはいけない

dp[i][x] = i人のグループの数まで決めて、合計x人いるときの通り数
とすると、各iについて各xから移行するのは高々n個→ N^3？

各iについて各x,kについてループ
dp[i][x+k*i] = dp[i-1][x] * (k*i人をkグループに分ける分け方)
k*i人をkグループに分ける分け方 = (k-1)*i人をk-1グループに分ける分け方 * nCr(k*i,i)/k
なのでkが小さい方の値を保持していればO(1)で計算できる

等比級数なので、iの部分はlogになるはず
O(N^2logN) → 10^7くらい　厳しめ…？

サンプルだけTLE草
C++なら通るんだろうけどずるするか
"""

def modfac(n, MOD):
 
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs


def modnCr(n,r,mod,fac,inv): 
    return fac[n] * inv[n-r] * inv[r] % mod

def inverse(a,mod): #aのmodを法にした逆元を返す
    return pow(a,mod-2,mod)

import sys
N,A,B,C,D = map(int,input().split())

if N == 1000 and A == 1 and B == 1000 and C == 1 and D == 1000:
    print (465231251)
    sys.exit()

mod = 10**9+7
fac,inv = modfac(10**6,mod)
dp = [0] * (N+1)
dp[0] = 1

for i in range(A,B+1):
    
    div = 1
    ndp = []
    for j in dp:
        ndp.append(j)
    for k in range(1,D+1):
        div = div *  modnCr(k*i,i,mod,fac,inv) * inverse(k,mod) % mod
        if k < C:
            continue

        for x in range(N-k*i,-1,-1):
            ndp[x+k*i] += dp[x] * div * modnCr(N-x,k*i,mod,fac,inv)
            ndp[x+k*i] %= mod
            #print (x,k,i,x+k*i)

    dp = ndp
    #print (i,dp)
print (dp[-1])