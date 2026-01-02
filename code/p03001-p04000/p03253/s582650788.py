MOD = 10 ** 9 + 7

def mod_pow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return mod_pow(a, p // 2) ** 2 % MOD
    else:
        return a * mod_pow(a, p - 1) % MOD

def calc_comb(a, b):
    if b > a - b:
        return calc_comb(a, a - b)
    ans_mul, ans_div = 1, 1
    for i in range(b):
        ans_mul *= a - i
        ans_div *= i + 1
        ans_mul %= MOD
        ans_div %= MOD
    return ans_mul * mod_pow(ans_div, MOD - 2) % MOD

def main():
    N, M = map(int, input().split())
    i = 2
    ans = 1
    while i * i <= M:
        if M % i == 0:
            cnt = 0
            while M % i == 0:
                cnt += 1
                M //= i
            ans *= calc_comb(N + cnt - 1, N - 1)
            ans %= MOD
        i += 1
    if M > 1:
        ans *= calc_comb(N + 1 - 1, N - 1)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()