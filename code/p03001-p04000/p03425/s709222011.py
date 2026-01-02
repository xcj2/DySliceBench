#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]"):
    count = [0] * 5
    for s in S:
        if s[0] in 'MARCH':
            idx = 'MARCH'.find(s[0])
            count[idx] += 1
    ret = 0
    for i1 in range(5):
        for i2 in range(i1 + 1, 5):
            for i3 in range(i2 + 1, 5):
                ret += count[i1] * count[i2] * count[i3]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [ next(tokens) for _ in range(N) ]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
