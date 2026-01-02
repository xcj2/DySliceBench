mod = 1000000007
fact = []
fact_inv = []
pow_ = []

def pow_ini(nn):
	global pow_
	pow_.append(nn)
	for j in range(62):
		nxt = pow_[j] * pow_[j]
		nxt %= mod
		pow_.append(nxt)
	return

def pow1(k):
    ansk = 1
    for ntmp in range(62):
        if((k >> ntmp) % 2 == 1):
            ansk *= pow_[ntmp]
            ansk %= mod
    return ansk

def fact_ini(n):
	global fact
	global fact_inv
	for i in range(n + 1):
		fact.append(0)
		fact_inv.append(0)
	fact[0] = 1
	for i in range(1, n + 1, 1):
		fact_tmp = fact[i - 1] * i
		fact_tmp %= mod
		fact[i] = fact_tmp
	pow_ini(fact[n])
	fact_inv[n] = pow1(mod - 2)
	for i in range(n - 1, -1, -1):
		fact_inv[i] = fact_inv[i + 1] * (i + 1)
		fact_inv[i] %= mod
	return

def nCm(n, m):
	assert(m >= 0)
	assert(n >= m)
	ans = fact[n] * fact_inv[m]
	ans %= mod
	ans *= fact_inv[n - m]
	ans %= mod
	return ans;

def nPm(n, m):
	assert(m >= 0)
	assert(n >= m)
	ans = fact[n]
	ans *= fact_inv[n - m]
	ans %= mod
	return ans;

fact_ini(5500000)
N, M = (int(x) for x in input().split())
ans = 0
for i in range(0, N+1, 1):
	anstmp = nCm(N, i) * nPm(M-i, N-i)
	anstmp %= mod
	if(i%2 == 1):
		anstmp *= -1
		anstmp += mod
		anstmp %= mod
	ans += anstmp
	ans %= mod
ans *= nPm(M, N)
ans %= mod
print(ans)