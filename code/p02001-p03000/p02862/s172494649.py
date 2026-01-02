X, Y = map(int,input().split())

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


def comb(m,n):
    MOD = 10**9 + 7
    fac, ifac = make_tables(MOD, m)
    ans = cmb(m, n, MOD, fac, ifac)
    return ans

def calculate(x,y):
    m = 0
    n = 0

    if ((x + y) % 3) != 0:
        print(0)
        return

    result = []

    while (2*m <= x) and (m <= y):
        n = x - 2 * m
        if (2*m + n == x) and (2*n + m == y):
            result.append(comb(m+n,n))

        m = m + 1

    if len(result) == 0:
        print(0)
    else:
        print(min(result))

calculate(X,Y)