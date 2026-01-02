#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

# 逆元comb
def comb(n, k):
    k = min(n-k,k)
    ans = 1
    for i in range(1, k + 1):
        ans *= (n + 1 - i) * pow(i,MOD-2,MOD)
        ans %= MOD
    return ans

def solve(n: int, a: int, b: int):
    comb_sum = pow(2,n,MOD)
    aa = comb(n,a)
    bb = comb(n,b)

    print((comb_sum-1-aa-bb)%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(n, a, b)

if __name__ == '__main__':
    main()
