from itertools import combinations
# from math import factorial as f
def cmb(n, k, mod, fac, ifac):
    """
    nCkを計算する
    """
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % mod


def make_tables(mod, n):
    """
    階乗テーブル、逆元の階乗テーブルを作成する
    """
    fac = [1, 1] # 階乗テーブル・・・(1)
    ifac = [1, 1] #逆元の階乗テーブル・・・(2)
    inverse = [0, 1] #逆元テーブル・・・(3)

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac

MOD = 10**9 + 7
def main():
    X, Y = map(int, input().split())
    a = 2 * X - Y
    if a % 3 != 0 or a < 0:
        print(0)
        return
    a = a // 3

    b = 2 * Y - X
    if b % 3 != 0 or b < 0:
        print(0)
        return
    b = b // 3

    total = a + b
    fac, ifac = make_tables(MOD, total)
    ans = cmb(a+b, min(a, b), MOD, fac, ifac)
    print(ans)


main()