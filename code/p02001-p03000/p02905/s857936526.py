MOD = 998244353

def zeta_gcd(a,primes):
    n = len(a)-1
    for p in primes:
        for i in range(n//p,0,-1):
            a[i] += a[p*i]
            a[i] %= MOD
def mobius_gcd(a,primes):
    n = len(a)
    for p in primes:
        for i in range(1,n):
            if i*p >= n: break
            a[i] -= a[p*i] 
            a[i] %= MOD
def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

NNN = 10**6 + 1
inverse = [0, 1]
for i in range( 2, NNN + 1 ):
    inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )

N, = map(int, input().split())
X = list(map(int, input().split()))
primes = get_primes(NNN)
fs = [0]*NNN
for x in X:
    fs[x] += x
#print(fs)
zeta_gcd(fs, primes)
#print(fs)
for i, x in enumerate(fs):
    fs[i] = x**2
#print(fs)
mobius_gcd(fs, primes)
#print(fs)
r = 0
for i, f in enumerate(fs[1:]):
    i += 1
    r = (r + f*inverse[i]) % MOD
for x in X:
    r = (r - x) % MOD

print((r*inverse[2])%MOD)
