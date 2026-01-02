import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

MOD = 10**9 + 7


def cmb(n, k, fac, ifac):
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % MOD


def make_table(n):
    fac = [1, 1]
    ifac = [1, 1]
    inverse = [0, 1]

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % MOD)
        inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
        ifac.append((ifac[-1] * inverse[-1]) % MOD)
    return fac, ifac


def main():
    X, Y = map(int, input().split())

    if X > Y:
        X, Y = Y, X
    dist = X + Y

    if dist % 3 != 0:
        print(0)
        exit()

    total = int((X+Y) / 3)
    n = X - total

    if Y > 2 * X:
        print(0)
    else:
        fac, ifac = make_table(total)
        ans = cmb(total, n, fac, ifac)
        print(ans)


if __name__ == '__main__':
    main()
