# 拡張ユークリッド互除法
# ax + by = gcd(a,b)の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def comb(n, max_k, mod):
    """
    (n,k) := n個からk個選ぶ組み合わせ
    k = 0~max_Kまでを計算して返す
    """
    res = [1]*(max_k+1)
    t = 1
    for i in range(max_k+1):
        res[i] *= t
        t *= n-i
        t %= mod

    n = reduce(lambda x,y: (x*y)%mod, range(1,max_k+1), 1)
    n = modinv(n, mod)

    for i in reversed(range(max_k+1)):
        res[i] *= n
        res[i] %= mod
        n *= i
        n %= mod
    return res

from functools import reduce
def solve(N,K):
    MOD = 10**9+7


    r1 = comb(N-K+1, min(K, N-K+1), MOD)
    r2 = comb(K-1, K-1, MOD)

    r1 += [0]*max(0,K+1-len(r1))
    return [(a*b)%MOD for a,b in zip(r1[1:],r2)]


if __name__ == '__main__':
    N,K = map(int,input().split())
    print(*solve(N,K), sep='\n')