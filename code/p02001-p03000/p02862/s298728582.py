import sys


def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2] // w[2]
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    return [w[0], w[1]]


def mod_inv(a, m):
    x = extgcd(a, m)[0]
    return (m + x % m) % m


def main():
    X, Y = map(int, input().split())
    C = 10**9 + 7

    if (X + Y) % 3 != 0:
        print(0)
        sys.exit()

    cnt = [0, 0]
    cnt[0] = (2 * X - Y) // 3
    cnt[1] = (-X + 2 * Y) // 3

    if cnt[0] < 0 or cnt[1] < 0:
        print(0)
        sys.exit()

    ans = 1
    for i in range(1, sum(cnt) + 1):
        ans *= i
        ans %= C
    for i in range(1, cnt[0] + 1):
        ans *= mod_inv(i, C)
        ans %= C
    for i in range(1, cnt[1] + 1):
        ans *= mod_inv(i, C)
        ans %= C

    print(ans)


main()
