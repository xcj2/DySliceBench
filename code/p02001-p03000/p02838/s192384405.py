#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int, A: "List[int]"):
    counts = [0] * 62
    for val in A:
        i = 0
        while val > 0:
            counts[i] += val % 2
            val //= 2
            i += 1
    ret = 0
    for i, cnt in enumerate(counts):
        ret += (2 ** i) * (cnt) * (N - cnt)
        ret %= MOD
    print(ret)
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
