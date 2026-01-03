#!/usr/bin/env python3
import sys
INF = float("inf")


def Run_length_encoding(S: str):
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


def solve(S: str):
    rle = Run_length_encoding(S)
    print(len(rle)-1)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
