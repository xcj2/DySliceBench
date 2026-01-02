import functools

MOD = 10**9 + 7


def lcm(a, b) -> int:
    c, d = a, b
    while d != 0:
        c, d = d, c % d
    return a // c * b


def inv_mod(x):
    return pow(x, MOD - 2)


def pow(x: int, n: int) -> int:
    res = 1
    while n > 0:
        if n & 1 == 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1

    return res


def main():
    N = int(input())
    an = list(map(int, input().split()))

    lcm_an = functools.reduce(lcm, an)
    lcm_an %= MOD

    ans = 0
    for a in an:
        ans = (ans + lcm_an * inv_mod(a)) % MOD

    print(ans)


if __name__ == '__main__':
    main()
