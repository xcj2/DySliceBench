#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(n, s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    nums = counts.values()
    ret = 1
    for num in nums:
        ret *= num + 1
        ret %= MOD
    ret -= 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
