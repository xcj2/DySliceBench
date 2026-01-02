N = int(input())

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


#階乗の逆元を求める
fac_lim = 200000
fac = [None]*(fac_lim+1)
fac[0] = 1
for i in range(fac_lim):
    fac[i+1] = fac[i] * (i+1)
    fac[i+1] = fac[i + 1] % 1000000007

fac_inv = [None]*(fac_lim+1)
fac_inv[fac_lim] = power(fac[fac_lim], 1000000005)
for i in range(fac_lim, 0, -1):
    fac_inv[i-1] = (fac_inv[i] * i)  % 1000000007

def conv(a, b):
    return (fac[a] * fac_inv[a-b] * fac_inv[b]) % 1000000007

MOD = 10**9 + 7

C = [int(i) for i in input().split()]
C.sort(reverse=True)

ans = 0
for i in range(N):
    ans += C[i] * (1+divide(i, 2))

ans *= power(2, 2*N-1)
ans %= MOD

print(ans)