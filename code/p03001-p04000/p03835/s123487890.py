#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(K: int, S: int):
    ret = 0
    for i in range(K + 1):
        for j in range(K + 1):
            if 0 <= S - (i + j) <= K:
                ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(K, S)

if __name__ == '__main__':
    main()
