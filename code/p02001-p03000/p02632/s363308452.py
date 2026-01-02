mod = 1000000007
fact = []
fact_inv = []
pow_ = []
pow25_ = []
pow26_ = []

def pow_ini(nn):
	global pow_
	pow_.append(nn)
	for j in range(62):
		nxt = pow_[j] * pow_[j]
		nxt %= mod
		pow_.append(nxt)
	return

def pow_ini25(nn):
	global pow25_
	pow25_.append(nn)
	for j in range(62):
		nxt = pow25_[j] * pow25_[j]
		nxt %= mod
		pow25_.append(nxt)
	return

def pow_ini26(nn):
	global pow26_
	pow26_.append(nn)
	for j in range(62):
		nxt = pow26_[j] * pow26_[j]
		nxt %= mod
		pow26_.append(nxt)
	return

def pow1(k):
	ansk = 1
	for ntmp in range(62):
		if((k >> ntmp) % 2 == 1):
			ansk *= pow_[ntmp]
			ansk %= mod
	return ansk

def pow25(k):
	ansk = 1
	for ntmp in range(31):
		if((k >> ntmp) % 2 == 1):
			ansk *= pow25_[ntmp]
			ansk %= mod
	return ansk

def pow26(k):
	ansk = 1
	for ntmp in range(31):
		if((k >> ntmp) % 2 == 1):
			ansk *= pow26_[ntmp]
			ansk %= mod
	return ansk

def fact_ini(n):
	global fact
	global fact_inv
	global pow_
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

fact_ini(2200000)
pow_ini25(25)
pow_ini26(26)
K = int(input())
S = input()
N = len(S)
ans = 0
for k in range(0, K+1, 1):
	n = N + K - k
	anstmp = 1
	anstmp *= pow26(k)
	anstmp %= mod
	anstmp *= nCm(n - 1, N - 1)
	anstmp %= mod
	anstmp *= pow25(n - N)
	anstmp %= mod
	ans += anstmp
	ans %= mod
print(ans)