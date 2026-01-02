#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(N: int, M: int, a: "List[int]"):
    p = [0] * (N+1)
    p[0] = 1

    for m in range(M-1):
        if a[m] + 1 == a[m + 1]:
            print(0)
            return

    a += [999999, 1999999]
    watch = 0
    if a[watch] == 1:
        watch += 1
        p[1] = 0
    else:
        p[1] = 1
    for n in range(2, N+1):
        if a[watch] == n:
            p[n] = 0
        elif a[watch] == n - 1:
            p[n] = p[n-2]
        elif a[watch] == n - 2:
            if a[watch+1] != n:
                p[n] = p[n-1]
            else:
                p[n] = 0
            watch += 1
        else:
            p[n] = p[n-1] + p[n-2]
    print(p[N] % MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    solve(N, M, a)

if __name__ == '__main__':
    main()
