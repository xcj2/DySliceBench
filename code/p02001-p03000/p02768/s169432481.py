# 二項係数を"やるだけ"にしてくれるライブラリ
MAX = 1000005
MOD = 10**9+7
factrial = [0]*MAX
inverse = [0]*MAX
factrial_inverse = [0]*MAX


# テーブルを作る前処理
def COMinit():
    global factrial, inverse, factrial_inverse
    factrial[0] = 1
    factrial[1] = 1
    inverse[1] = 1
    factrial_inverse[0] = 1
    factrial_inverse[1] = 1
    for i in range(2, MAX):
        factrial[i] = factrial[i-1] * i % MOD
        inverse[i] = MOD - inverse[MOD % i] * (MOD//i) % MOD
        factrial_inverse[i] = factrial_inverse[i-1] * inverse[i] % MOD


# 二項係数計算
def COM(n, k):
    global factrial, inverse, factrial_inverse
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return factrial[n] * (factrial_inverse[k] * factrial_inverse[n-k] % MOD) % MOD


# 前処理完了
COMinit()


def pow_r(x, n):
    """
    O(log n)
    """
    if n == 0:  # exit case
        return 1
    if n % 2 == 0:  # standard case ① n is even
        return pow_r((x ** 2) % MOD, n // 2) % MOD
    else:  # standard case ② n is odd
        return x * pow_r((x ** 2) % MOD, (n - 1) // 2) % MOD


N, A, B = map(int, input().split())
MOD = 1000000007
all_number = (pow_r(2, N)-1)
# nがさらに巨大な時
tmp_A = 1
for i in range(1, A+1):
    tmp_A %= MOD
    tmp_A *= (N-i+1)
    tmp_A *= inverse[i]

tmp_B = 1
for i in range(1, B+1):
    tmp_B %= MOD
    tmp_B *= (N-i+1)
    tmp_B *= inverse[i]
tmp_A %= MOD
tmp_B %= MOD
# print(all_number, tmp_A, tmp_B)
ans = (all_number - (tmp_A+tmp_B) + MOD)%MOD
print(ans % MOD)
