# https://atcoder.jp/contests/abc156/tasks/abc156_d

import sys
input = sys.stdin.readline


from operator import mul
from functools import reduce

def pow_k(x, n, mod):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
            K %= mod
        x *= x
        x %= mod
        n //= 2

    return (K * x) %mod


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

def main():
    n, a, b = [int(i) for i in input().strip().split()]
    MOD = 10**9 + 7
    _sum = ((pow_k(2, n,MOD))-1) % MOD
    cmb_a = combination(n, a,MOD)
    cmb_b = combination(n, b,MOD)
    ans = (_sum - cmb_a - cmb_b) % MOD
    
    print(ans)

if __name__ == "__main__":
    main()