#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, S: str):

    comp = [0]
    for pre, curr in zip(S[0]+S, S):
        if pre == curr:
            comp[-1] += 1
        else:
            comp.append(1)

    print(sum(comp)-max(len(comp)-2*K, 1))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)


if __name__ == '__main__':
    main()
