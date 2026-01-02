#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(S: str):
    counter = Counter(S)
    for i in range(ord("a"), ord("z")+1):
        if counter[chr(i)] == 0:
            break
    else:
        print("None")
        return
    print(chr(i))

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
