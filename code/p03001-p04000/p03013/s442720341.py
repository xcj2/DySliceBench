MOD = 1000000007

fact = [0 for i in range(100001)] # fact[i] = i! mod MOD
inv_fact = [0 for i in range(100001)] # inv_fact[i] = i!のmod MODでの逆元
 
# aのn乗をPで割った余りを求めるよ
def mod_pow(a, n, P):
	if n == 0: # aの0乗は1（それはそう）
		return 1
	if n%2 == 0: # aの4乗は（aの2乗）の2乗、みたいなノリ
		x = mod_pow(a, n/2, P)
		return (x*x)%P
	# aの5乗はa×（aの4乗）、みたいなノリ
	return (a*mod_pow(a, n-1, P))%P
 
# nCk mod MODを求める！！
def comb(n, k):
	if n < k:
		return 0
	ans = fact[n]
	ans = (ans * inv_fact[k])%MOD
	ans = (ans * inv_fact[n-k])%MOD
	return ans

def move(n):
	twonum = n // 2
	com = 0
	for i in range(twonum + 1):
		up = n - i
		com += comb(up, i)
	return com

# fact,inv_factを初期化
fact[0] = inv_fact[0] = 1
for i in range(100000):
	# (i+1)!ってi!に(i+1)をかけたものだよね
	fact[i+1] = (fact[i]*(i+1))%MOD
	# (i+1)!の逆元って、i!の逆元に(i+1)の逆元をかけたものだよね
	inv_fact[i+1] = (inv_fact[i]*mod_pow(i+1, MOD-2, MOD))%MOD

N, M = map(int, input().split())
a = []
a.append(0)
for i in range(M):
	a.append(int(input()))
a.append(N+1)

s = 1
for i in range(M+1):
	step = a[i+1] - a[i] - 1
	if step > MOD:
		step = step % MOD
	m = move(step)
	s = (s * m) % MOD
	a[i+1] += 1

print(s)
