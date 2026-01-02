
import math


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def prime_fact(x):
    prime_pow = {}
    check_ceil = math.ceil(math.sqrt(x))
    for p in range(2, check_ceil + 1):
        p_cnt = 0
        while x % p == 0:
            x //= p
            p_cnt += 1
        if p_cnt:
            prime_pow[p] = p_cnt
    if x > 1:
        prime_pow[x] = 1
    return prime_pow


def submit():
    a, b = map(int, input().split())
    g = gcd(a, b)
    # gcdの素因数分解して素因数の数を求める
    p = prime_fact(g)
    print(len(p) + 1)


if __name__ == "__main__":
    submit()
