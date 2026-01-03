#!/usr/bin/env python3
import sys
from math import sqrt

def solve(N: int, X: int):
    # 平行四辺形の面積
    answer = N
    a,b = max(N-X,X),min(N-X,X)
    while True:
        answer += 2*(a//b)*b
        if a%b == 0:
            answer -= b
            break
        a,b = b,a%b

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(N, X)

if __name__ == '__main__':
    main()
