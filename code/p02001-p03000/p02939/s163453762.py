#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(S: str):
    N = len(S)
    count = 1
    pre = 0
    curr = 1
    while True:
        for i in range(1, 100):
            if S[pre:curr] != S[curr:curr+i]:
                break
            if curr+i >= N:
                break
        if curr+i >= N:
            break
        pre = curr
        curr = curr+i
        count += 1
    if S[pre:curr] != S[curr:curr+i]:
        pre = curr
        curr = curr+i
        count += 1

    print(count)

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
