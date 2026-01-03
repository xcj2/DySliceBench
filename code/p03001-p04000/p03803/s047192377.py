#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(A: int, B: int):
    ret = 'Draw'
    if A != B:
        if A == 1 :
            ret = 'Alice'
        elif B == 1 :
            ret = 'Bob'
        elif A > B :
            ret = 'Alice'
        else:
            ret = 'Bob'
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
