#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().strip()

MOD = 1000000007  # type: int

def modinv(x):
    return pow(x, MOD - 2, MOD)

def solve(N: int, A: "List[int]"):
    factors = [0 for i in range(10**6 + 1)]
    for x in A:
        i = 2
        while i * i <= x:
            curr = 0
            while x % i == 0:
                curr += 1
                x //= i
            factors[i] = max(factors[i], curr)
            i += 1
        if x > 1:
            factors[x] = max(factors[x], 1)
    lcm = 1
    for i in range(10**6 + 1):
        lcm *= pow(i, factors[i], MOD)
        lcm %= MOD
    ans = 0
    for ai in A:
        ans += lcm * modinv(ai) % MOD
        ans %= MOD
    print(ans)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
