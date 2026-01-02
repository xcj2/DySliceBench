n,k =  list(map(int, input().split() ))


# 二項係数を 10^9+7 で割った余りを求める
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#5-%E4%BA%8C%E9%A0%85%E4%BF%82%E6%95%B0-ncr
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6

mod = 10**9 + 7

# x ** a をmodで割った余りを、lod(a)時間で求める。
def power(x, a):
	if a == 0:
		return 1
	elif a == 1:
		return x
	elif a % 2 == 0:
		return power(x, a//2) **2 % mod
	else:
		return power(x, a//2) **2 * x % mod

# xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はlog(mod)程度。
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
def modinv(x):
	return power(x, mod-2)

# 二項係数の左側の数字の最大値を max_len　とする。nとかだと他の変数と被りそうなので。
# factori_table = [1, 1, 2, 6, 24, 120, ...] 要は factori_table[n] = n!
max_len = n #適宜変更する

factori_table = [1] * (max_len + 1)
factori_inv_table = [1] * (max_len + 1)
for i in range(1, max_len + 1):
	factori_table[i] = factori_table[i-1] * (i) % mod
	factori_inv_table[i] = modinv(factori_table[i])

def binomial_coefficients(n, k):
	# n! / (k! * (n-k)! )
	return (factori_table[n] * factori_inv_table[k] * factori_inv_table[n-k]) % mod

for i in range(1, k+1):
	if i-1 > n-k:
		# 境界を i-1 個作らなければならないが、赤いボールの数 n-k よりもこれが多いと条件を満たす置き方は存在しない
		print(0)
	else:
		# (n-k+1)C(i) * (k-1)C(k-i)
		print((binomial_coefficients(n-k+1, i) * binomial_coefficients(k-1, k-i)) % mod)

		