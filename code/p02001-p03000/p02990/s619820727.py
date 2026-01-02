import math
 
MOD = 1000000000 + 7
 
def egcd(a, b):
    if a ==  0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return (g, x - (b//a) * y, y)
 
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("No inverse exists")
    else:
        return x % m
 
def combination(n, r):
    return math.factorial(n)%MOD * modinv(math.factorial(r), MOD) * modinv(math.factorial(n-r), MOD) % MOD
    # return math.factorial(n) // math.factorial(r) // math.factorial(n-r)
 
N, K = [int(x) for x in input().split()]
 
for i in range(1, K+1):
    if N-K+1 < i:
        ans = 0
    else:
        ans = (combination(N-K+1, i) * math.factorial((K-i)+(i-1)))%MOD * (modinv(math.factorial(K-i), MOD)%MOD) * (modinv(math.factorial(i-1), MOD)%MOD)
 
    print(ans%MOD)
