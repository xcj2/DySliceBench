
def extended_gcd(a, b):
    c0, c1 = a, b
    a0, a1 = 1, 0
    b0, b1 = 0, 1

    while c1 != 0:
        q, m = divmod(c0, c1)
        c0, c1 = c1, m
        a0, a1 = a1, a0 - q*a1
        b0, b1 = b1, b0 - q*b1
    return a0, b0, c0


def mod_inverse(a, n):
    s, _, g = extended_gcd(a, n)
    if g != 1:
        raise Exception('The inverse does not exist.')
    return s % n

def comb(n, k):
    c = 1
    k = min(k, n-k)
    for i in range(k):
        c *= n-i
        c *= mod_inverse(i+1, MOD)
        c %= MOD
    return c

n,a,b=map(int, input().split())
MOD = 1000000007
ans = pow(2, n, MOD)
ans -= comb(n, a)
while ans < 0:
    ans += MOD
ans -= comb(n, b)
while ans < 0:
    ans += MOD
print(ans-1)
