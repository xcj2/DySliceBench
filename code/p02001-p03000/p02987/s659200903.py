#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str):
    c= collections.Counter(S)
    if c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
        print("Yes")
    else:
        print("No")

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
