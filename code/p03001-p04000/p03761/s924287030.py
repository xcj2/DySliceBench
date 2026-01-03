#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(n: int, S: "List[str]"):

    co = []
    for s in S:
        co.append(Counter(s))
    ans = ""
    for i in range(26):
        c = chr(ord("a")+i)
        num = min([x[c] for x in co])
        ans += c*num
    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(n)]  # type: "List[str]"
    solve(n, S)


if __name__ == '__main__':
    main()
