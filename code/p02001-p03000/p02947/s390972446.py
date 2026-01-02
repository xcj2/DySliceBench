#!/usr/bin/env python3
import sys
import collections
from itertools import groupby

def solve(N: int, s: "List[str]"):
    s = [sorted(s[i]) for i in range(N)]
    s.sort()
    group = groupby(s)
    answer = 0
    for _, group in group:
        a = len(list(group))
        answer += int(a*(a-1)/2) if a > 1 else 0
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, s)

if __name__ == '__main__':
    main()
