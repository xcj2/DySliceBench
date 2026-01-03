#!/usr/bin/env python3
import sys


def solve(K: int, S: int):
    cnt=0
    x_max = S if K >= S else K
    for x in range(0, x_max+1):
        y_max = S-x if K >= S-x else K
        for y in range(0, y_max+1):
            z = S - x - y
            if z <= K:
                cnt+=1
    return cnt


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    print(solve(K, S))

if __name__ == '__main__':
    main()
