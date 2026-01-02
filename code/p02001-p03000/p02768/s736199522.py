n, a, b = list(map(int, input().split()))

mod = 10**9 + 7

import time
start = time.time()


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
	return pow(x, mod-2, mod)

modinv_table = [-1] * (b+1)
for i in range(1, b+1):
    modinv_table[i] = modinv(i)

end = time.time()
# print("time: ", end - start)

def binomial_coefficients2(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans

# (2 ** n - 1) - nCa - nCb
ans = power(2, n) - 1

ans -= (binomial_coefficients2(n, a) + binomial_coefficients2(n, b))
print(ans % mod)


# print(binomial_coefficients2 (5, 2) % mod)
