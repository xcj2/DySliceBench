#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().strip()

def C(first, last, ndigs, N):
    ans = 0
    curr = first * 10 ** (ndigs - 1) + (last if ndigs > 1 else 0)
    incs = 0
    while curr <= N and incs < 10 ** (ndigs - 1):
        ans += 1
        curr += 10
        incs += 10
    return ans

def solve(N: int):
    ndigs = len(str(N))
    ans = 0
    for ndigsA in range(1, ndigs + 1):
        for ndigsB in range(1, ndigs + 1):
            for first in range(1, 10):
                for last in range(1, 10):
                    if (ndigsA > 1 and ndigsB > 1) or first == last:
                        ans += C(first, last, ndigsA, N) * C(last, first, ndigsB, N)
    print(ans)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
