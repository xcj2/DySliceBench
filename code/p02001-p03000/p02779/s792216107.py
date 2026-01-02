#!/usr/bin/env python3
import sys
INF = float("inf")
from collections import Counter


def yes():
    print("YES")  # type: str


def no():
    print("NO")  # type: str


def solve(N: int, A: "List[int]"):
    counter = Counter()
    flag = True
    for a in A:
        counter[a] += 1
        if counter[a] > 1:
            flag = False
            break
    if flag:
        yes()
    else:
        no()

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
