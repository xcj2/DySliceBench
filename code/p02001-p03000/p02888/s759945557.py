#!/usr/bin/env python3
import sys
import bisect


def solve(N: int, L: "List[int]"):
    L.sort()
    cnt=0
    for a_i in range(N):
        for b_i in range(a_i+1, N):
            c_r = bisect.bisect_left(L, L[a_i]+L[b_i])
            cnt += c_r - b_i - 1
    return cnt


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, L))

if __name__ == '__main__':
    main()
