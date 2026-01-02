#!/usr/bin/env python3
import sys
INF = float("inf")


def Run_length_encoding(S: str):
    """AAABBC -> [(A, 3), (B, 2), (C, 1)]
    """
    ans = []
    curr = S[0]
    counter = 0
    for c in S:
        if c == curr:
            counter += 1
        else:
            ans.append((curr, counter))
            curr = c
            counter = 1
    ans.append((curr, counter))
    return ans


def solve(N: int, S: str):
    print(len(Run_length_encoding(S)))
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
