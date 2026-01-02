n, a, b = map(int, input().split())
mod = 10**9+7
"""
def factorial_mod(x, y, mod):
    factorial = 1
    for i in range(x,y+1):
        factorial *= i
        factorial %= mod
    return factorial


#conbinationを何回も求める場合はfactorial_k,nkをあらかじめ計算し, リストに入れておけば良い
def n_C_k(n,k,mod):
    factorial_nk = factorial_mod(n-k+1, n, mod)
    factorial_k = factorial_mod(1,k,mod)
    conbi=factorial_nk*pow(factorial_k, mod-2, mod)
    return conbi%mod

ans = (pow(2, n, mod)-1-n_C_k(n, a, mod)-n_C_k(n, b, mod))%mod
print(ans)
"""

#n!を求める
def factorial_mod(n, mod):
    x = 1
    for i in range(1, n+1):
        x *= i
        x %= mod
    return x

#n_P_kを求める
def permutation_mod(n, k, mod):
    x = 1
    for i in range(n-k+1, n+1): #k回for文を回す
        x *= i
        x %= mod
    return x

#conbinationを何回も求める場合はfactorial_k,nkをあらかじめ計算し, リストに入れておけば良い
def n_C_k(n, k, mod): #O(min(k, n-k))
    k = min(k, n-k)
    n_P_k = permutation_mod(n, k, mod)
    factorial_k = factorial_mod(k, mod)
    conbi=n_P_k * pow(factorial_k, mod-2, mod)
    return conbi % mod

ans = (pow(2, n, mod)-1-n_C_k(n, a, mod)-n_C_k(n, b, mod))%mod
print(ans)