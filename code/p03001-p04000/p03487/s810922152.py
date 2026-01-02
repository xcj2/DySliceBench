#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(N: int, a: "List[int]"):
    counter = Counter(a)

    ans = 0
    for key in counter:
        if counter[key] < key:
            ans += counter[key]
        else:
            ans += counter[key]-key
    print(ans)
    return


a = []
for i in range(1, 10):
    a.extend([i]*3)

counter = Counter(a)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
