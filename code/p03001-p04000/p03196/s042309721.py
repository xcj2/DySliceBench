#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, P: int):
    def primeFactorize(n: int):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    # print(primeFactorize(P))
    from collections import Counter
    c = Counter(primeFactorize(P))

    ans = 1
    for k, v in c.most_common():
        if v >= N:
            ans *= k**(v//N)


    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(N, P)

if __name__ == '__main__':
    main()
