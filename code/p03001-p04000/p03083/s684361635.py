#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def get_z(y, x): # y/x (mod 1000000007)
    inv_x = pow(x, MOD - 2, MOD)
    return y * inv_x % MOD

def _get_z(y, x): # y / x
    #inv_x = pow(x, MOD - 2, MOD)
    #return y * inv_x % MOD
    while y % x > 0:
        y += MOD
    return y // x

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def reduce(y, x):
    tmp = gcd(x, y)
    return (y // tmp, x // tmp)

def make_comb(n, k):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    ret = [0] * (n + 1)
    for i in range(k, n + 1):
        a = fact[i]
        b = (fact[k] * fact[i - k]) % MOD
        ret[i] = get_z(a, b)
    return ret

def _make_comb(n, k):
    ret = [0] * n
    ret[k] = 1
    for i in range(k + 1, n):
        ret[i] = (ret[i - 1] * i) // (i - k)
        ret[i] %= MOD
    return ret

def solve(b: int, w: int):
    n = b + w
    bb = 0
    ww = 0
    b_comb = make_comb(n, b - 1)
    w_comb = make_comb(n, w - 1)
    par = 1
    for i in range(1, n + 1):
        #print(' ======== i: %d ==============' % i)
        other = par - bb - ww
        x = (par * 2) % MOD
        y = (other + bb * 2) % MOD
        #x = (par * 2)
        #y = other + bb * 2
        #print("bb : %d, ww : %d, other : %d" % (bb, ww, other))
        #print(y, ' / ', x)
        #y, x = reduce(y, x)
        ret = get_z(y, x)
        print(ret)
        #bb = (bb * 2 + w_comb[i - 1])
        #ww = (ww * 2 + b_comb[i - 1])
        #par = (par * 2)
        bb = (bb * 2 + w_comb[i - 1]) % MOD
        ww = (ww * 2 + b_comb[i - 1]) % MOD
        par = (par * 2) % MOD
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    B = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(B, W)

if __name__ == '__main__':
    main()
