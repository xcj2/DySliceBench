#!/usr/bin/env python3
import sys
import numpy as np


def solve(N: int, p: "List[int]"):
    sorted_list = [i for i in range(1, N + 1)]
    if p == sorted_list:
        print("YES")
    elif N - sum(np.array(p) == sorted_list) == 2:
        print("YES")
    else:
        print("NO")


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)


if __name__ == "__main__":
    main()
