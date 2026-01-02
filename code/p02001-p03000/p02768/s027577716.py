n, a, b = list(map(int, input().split()))

mod = 10**9 + 7

# x ** a をmodで割った余りを、O(log(a))時間で求める。
def power(x, a):
	if a == 0:
		return 1
	elif a == 1:
		return x
	elif a % 2 == 0:
		return power(x, a//2) **2 % mod
	else:
		return power(x, a//2) **2 * x % mod


# xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
def modinv(x):
	return power(x, mod-2)

mod_table = [-1] * (b+1)
mod_table[1] = 1
for i in range(2, b+1):
    mod_table[i] = (mod_table[i - 1] * (i)) % mod

def binomial_coefficients2(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans %= mod
    ans *= modinv(mod_table[k])
    return ans % mod

# (2 ** n - 1) - nCa - nCb
ans = power(2, n) - 1

ans -= (binomial_coefficients2(n, a) + binomial_coefficients2(n, b))
print(ans % mod)
