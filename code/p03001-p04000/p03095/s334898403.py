#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int
from collections import Counter
from itertools import product
def solve(N: int, S: str):
    counter = dict(Counter(S))
    values = list(counter.values())
    LEN = len(values)
    answer = values[0]+1
    if LEN >= 2:
        for i in range(1,LEN):
            answer *= values[i]+1
            answer%=MOD
    print(answer-1)
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
