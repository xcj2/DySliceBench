#!/usr/bin/env python3
import sys


def z_algo(N, S):
    end = 1
    start = 0
    max_length = 0

    while start < N:
        while end-start > N-end:
            break
        subword = S[start:end]
        if subword in S[end:]:
            max_length = max(max_length, len(subword))
            end += 1
        else:
            start += 1
            if start == end:
                end += 1
    return max_length


def solve(N: int, S: str):
    print(z_algo(N, S))
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
