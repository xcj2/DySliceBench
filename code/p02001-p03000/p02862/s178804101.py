import sys
import math
sys.setrecursionlimit(200000)
MOD = 10 ** 9 + 7


def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2] // w[2]
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0], w[1]]
# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)


def mod_inv(a,m):
    x = extgcd(a, m)[0]
    return (m + x % m) % m


def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        exit()
    else:
        m = (2 * X - Y) // 3
        n = (2 * Y - X) // 3
        if m < 0 or n < 0:
            print(0)
            exit()
        else:
            res = 1
            for i in range(1, n + m + 1):
                res = res * i % MOD
            for i in range(1, n + 1):
                res = res * mod_inv(i, MOD) % MOD
            for i in range(1,m + 1):
                res = res * mod_inv(i, MOD) % MOD
            print(res)

if __name__ == "__main__":
    main()
