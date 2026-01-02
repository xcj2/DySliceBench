#!/usr/bin/env python3
import sys
INF = 1<<32
MOD = 1000000007  # type: int

# def iterate_tokens():
#     for line in sys.stdin:
#         for word in line.split():
#             yield word
# tokens = iterate_tokens()
# n = int(next(tokens))  # type: int
# k = int(next(tokens))  # type: int


def solve(n: int, k: int):
    fact = [1] * (n+1)
    ifact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1] % MOD

    ifact[-1] = pow(fact[-1], MOD-2, MOD)
    for i in range(n-1, 0, -1):
        ifact[i] = ifact[i+1] * (i+1) % MOD

    def comb(n, r, MOD=10**9+7):
        return fact[n] * ifact[n-r] * ifact[r] % MOD
    
    
    ans = 0
    for i in range(min(k, n-1)+1):
        ans += comb(n, i) * comb(n-1, i) % MOD
        ans %= MOD
    
    print(ans)

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(n, k)

if __name__ == '__main__':
    main()