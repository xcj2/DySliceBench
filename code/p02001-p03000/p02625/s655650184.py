N,M = map(int,input().split())
mod = 10**9+7

def plmi(k):
    if k%2 == 0:
        return 1
    else:
        return -1

# 1!,2!,3!,...,n! (mod m)
def mod_factorials(n, m):
    mod_factorials = [1] * (n + 1)
    for i in range(1, n+1):
        mod_factorials[i] = mod_factorials[i-1]*i
        mod_factorials[i] %= m
    return mod_factorials

# 1!,2!,3!,...,n! の逆元 (mod m)
def mod_inv_factorials(n, m):
    mod_invs = [1] * (n + 1)
    invs = [1] * (n + 1)
    for i in range(2, n + 1):
        invs[i] = m - invs[m % i] * (m//i) % m

    for i in range(1, n+1):
        mod_invs[i] = invs[i]*mod_invs[i-1]
        mod_invs[i] %= m
    return mod_invs

mod_facts = mod_factorials(M,mod)
mod_inv_facts = mod_inv_factorials(M,mod)

ans = 0

for i in range(0,N+1):
    tmp = 1
    tmp *= plmi(i)*mod_facts[N]*mod_facts[M-i]*mod_inv_facts[i]*mod_inv_facts[N-i]*mod_inv_facts[M-N]
    ans += tmp
    ans %= mod

ans *= mod_facts[M]*mod_inv_facts[M-N]
ans %= mod

print(ans)







