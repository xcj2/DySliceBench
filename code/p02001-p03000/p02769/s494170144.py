def make_tables(n, p):
    fac = [1, 1]  # 階乗テーブル
    ifac = [1, 1]  # 逆元の階乗テーブル
    inverse = [0, 1]  # 逆元テーブル

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % p)
        inverse.append((-inverse[p % i] * (p//i)) % p)
        ifac.append((ifac[-1] * inverse[-1]) % p)
    return fac, ifac

def cmb(n, r, p, fac, ifac):
    if r < 0 or r > n:
        return 0
    return fac[n] * ifac[r] * ifac[n-r] % p


def resolve():
    n, k = map(int, input().split())
    p = 10 ** 9 + 7
    
    k = min(n-1, k)
    sum = 0
    fac, ifac = make_tables(n, p)
    for i in range(0, k+1):
        sum += cmb(n, i, p, fac, ifac) * cmb(n-1, i, p, fac, ifac) % p

    print(sum % p)



if __name__ == "__main__":
    resolve()
