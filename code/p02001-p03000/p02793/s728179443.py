def kouyaku(a,b):
    aa = max(a,b)
    bb = min(a,b)
    if bb == 0:
        return aa
    else:
        return kouyaku(bb,aa%bb)

def power(a, b):
	if b == 0:
		return 1
	elif b == 1:
		return a % 1000000007
	elif b % 2 == 0:
		return (power(a, b//2) ** 2) % 1000000007
	else:
		return (power(a, b//2) ** 2 * a) % 1000000007
 
def divide(a, b):
	return (a * power(b, 1000000005)) % 1000000007

def prime(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > x**(1/2): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]

primes = prime(10**6)
pd = {}
for i in range(len(primes)):
	pd[primes[i]] = i
MOD = 10**9+7
N = int(input())
A = [int(i) for i in input().split()]
K = [0]*len(primes)
for i in range(N):
	a = A[i]
	for i in range(len(primes)):
		p = primes[i]
		if a == 1:
			break
		elif p > 1000:
			K[pd[a]] = 1
			break
		else:
			cou = 0
			while a%p==0:
				a = a//p
				cou += 1
			K[i] = max(cou, K[i])
kv = 1
for i in range(len(primes)):
	kv *= power(primes[i], K[i])
	kv %= MOD
ans = 0
for i in range(N):
	ans += divide(kv, A[i])
	ans %= MOD
print(ans)