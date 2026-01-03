#!/usr/bin/env python3
import sys
from collections import deque
INF = float("inf")


def solve(N: int, S: str):
    X = ""
    counter = 0                 # counterは(の数
    for i, c in enumerate(S):
        if c == ')' and counter == 0:
            X = '(' + X + ')'
        elif c == ')' and counter > 0:
            X = X + ')'
            counter -= 1
        elif c == '(':
            X = X + '('
            counter += 1
    X += ')'*counter
    print(X)
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
