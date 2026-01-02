X, Y = (int(i) for i in input().split())

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
fac_lim = 1000000
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
if (X+Y)%3 != 0:
    ans = 0
else:
    N = (X+Y)//3
    M = X - Y
    if (N+M)%2 !=0:
        ans = 0
    else:
        a = (N+M)//2
        if 0 <= a <= N:
            ans = conv(N, a)
        else:
            ans = 0
print(ans%MOD)