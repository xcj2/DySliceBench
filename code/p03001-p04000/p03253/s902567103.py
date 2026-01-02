MOD = 10**9 + 7

def power_mod(a,n):
    if n == 0:
        return 1
    x = (power_mod(a,n//2)**2)%MOD
    return x if n%2 == 0 else (a*x)%MOD

def inverse(a):
    return power_mod(a,MOD-2)

def comb(n,k):
    # k is small
    num = 1
    den = 1
    for i in range(1,k+1):
        num *= (n+1-i)
        den *= i
        num %= MOD
        den %= MOD
    return (num * inverse(den))%MOD

def solve(N,M,min_p=2):
    if M == 1:
        return 1
    for p in range(min_p, M+1):
        if p*p > M:
            # M is prime
            return N
        if M%p != 0:
            continue
        e = 0
        while M%p == 0:
            M //= p
            e += 1
        return (solve(N, M, p) * comb(N-1+e,e))%MOD
      
N,M = map(int, input().split())
ans = solve(N,M)

print(ans)