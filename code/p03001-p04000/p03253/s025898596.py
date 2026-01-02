# coding:utf-8

INF = float('inf')
MOD = 10 ** 9 + 7


def inpl(): return list(map(int, input().split()))


# aのp乗を求めるアルゴリズム
# MOD版
# O(logp)
def pow_mod(a, p):
    if p == 0: return 1
    if p % 2 == 0:
        half_p = p // 2
        half = pow_mod(a, half_p)

        return half * half % MOD
    else:
        return a * pow_mod(a, p - 1) % MOD


# 組み合わせnCrを求めるアルゴリズム
# 逆元を使って計算
# MOD版
def cmb_mod(n, r):
    # 5C3 -> 5C2
    if r > n - r: return cmb_mod(n, n - r)
    ans_mul = 1
    ans_div = 1
    for i in range(r):
        ans_mul *= n - i
        ans_div *= i + 1
        ans_mul %= MOD
        ans_div %= MOD

    # ans_mul / ans_divをしたい
    # ans_divの逆元を使って求める
    ans = ans_mul * pow_mod(ans_div, MOD - 2) % MOD
    return ans


N, M = inpl()
ans = 1
i = 2
while i * i <= M:
    if M % i == 0:
        cnt = 0
        while M % i == 0:
            cnt += 1
            M //= i
        ans *= cmb_mod(N - 1 + cnt, cnt)
        ans %= MOD
    i += 1

if M != 1:
    ans *= cmb_mod(N - 1 + 1, 1)
    ans %= MOD
print(ans)
