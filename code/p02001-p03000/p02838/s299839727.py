#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    ans = 0
    base = 1
    for i in range(60):
        counter = [0, 0]
        buf = 0
        for j in range(N):
            if A[j] & (1 << i):
                buf += counter[0]
                counter[1] += 1
            else:
                buf += counter[1]
                counter[0] += 1
        ans += buf * base
        ans %= MOD
        base = (base * 2) % MOD
    print(ans)
    return


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
