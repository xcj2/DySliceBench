def get_divisor(n):
    ret = []
    for i in range(3, n + 1, 2):
        if n % i == 0:
            ret.append(i)
    return ret


def get_dec(x, MOD):
    b = 1
    t = 0
    for c in x[::-1]:
        if c == '1':
            t = (t + b) % MOD
        b = b * 2 % MOD
    return t


def count_head_smaller(x, y, d, t, MOD):
    p = x[:t]
    q = y[:t]
    k = get_dec(p, MOD)
    r = (p + q) * (d // 2) + p
    if x >= r:
        k += 1
    return k


def solve(n, x):
    MOD = 998244353
    divisors = get_divisor(n)
    divisors.reverse()
    checked_divisors = {}

    y = ''.join('1' if c == '0' else '0' for c in x)

    ans = 0
    short = 0
    for d in divisors:
        t = n // d
        k = count_head_smaller(x, y, d, t, MOD)

        for pd, pk in checked_divisors.items():
            if pd % d != 0:
                continue
            k -= pk

        ans = (ans + 2 * t * k) % MOD
        short += k
        checked_divisors[d] = k

    t = (get_dec(x, MOD) + 1 - short) % MOD
    ans = (ans + t * 2 * n) % MOD
    return ans


n = int(input())
x = input()
print(solve(n, x))
