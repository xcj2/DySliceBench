#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(A: int, B: int):
    if len(A) > len(B):
        ret = 'GREATER'
    elif len(A) < len(B):
        ret = 'LESS'
    else:
        ret = 'EQUAL'
        for i in range(len(A)):
            if A[i] > B[i]:
                ret = 'GREATER'
                break
            elif A[i] < B[i]:
                ret = 'LESS'
                break
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = str(next(tokens))  # type: int
    B = str(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
