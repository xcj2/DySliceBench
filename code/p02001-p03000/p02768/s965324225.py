import math

def modpow(a, n, p):
    if n == 0:
        return 1
    elif n == 1:
        return a % p
    elif n%2 == 1:
        return (a * modpow(a, n-1, p)) % p
    else:
        temp = modpow(a, n//2, p)
        return (temp * temp) % p

def n_permutations(n, a):
    p = 7 + pow(10, 9)
    ans = 1
    for i in range(n-a+1, n+1):
        ans = ans * i
        ans = ans % p
    return ans

def permutations(a):
    p = 7 + pow(10, 9)
    ans = 1
    for i in range(1, a+1):
        ans = ans * i
        ans = ans % p
    return ans

n, a, b = map(int,input().split())
p = 7 + pow(10, 9)

ans = modpow(2, n, p) - 1
ans = ans - ((n_permutations(n, a) * modpow(permutations(a), (p-2), p))%p)
ans = ans - ((n_permutations(n, b) * modpow(permutations(b), (p-2), p))%p)

print(ans%p)
