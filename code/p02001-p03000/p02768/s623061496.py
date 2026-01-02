n, a, b = map(int, input().split())
p = 1000000007
def fast_pow(x,n,p):
    ans = 1
    while(n > 0):
        if n & 1 == 1:
            ans = ans * x % p
        x = x * x % p
        n = n >> 1
    return ans

def comb_mod(n, k, mod):
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % mod
        denominator = (denominator * (i + 1)) % mod

    return (numerator * fast_pow(denominator, mod - 2, mod)) % mod

def factor(a,b):
    ans = 1
    for i in range(a, b+1):
        ans*=i
    return ans

total = (fast_pow(2,n,p) - 1) % p
case_a = comb_mod(n, a, p)
case_b = comb_mod(n, b, p)

print((total - case_a - case_b) % p)