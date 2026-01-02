#!/usr/bin/env python3
import sys


def solve(M: "List[int]", D: "List[int]"):
    if M[0] != M[1]:
        print(1)
    else:
        print(0)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = [int()] * (2)  # type: "List[int]"
    D = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        M[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(M, D)

if __name__ == '__main__':
    main()
