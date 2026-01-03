#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(X: int, A: int, B: int):
    if B > X + A:
        ret = 'dangerous'
    elif B <= A:
        ret = 'delicious'
    else:
        ret = 'safe'
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(X, A, B)

if __name__ == '__main__':
    main()
