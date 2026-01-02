#!/usr/bin/env python3
import sys


def solve(N: int, s: "List[str]", t: "List[int]", X: str):
    index = s.index(X)
    print(sum(t[index+1:]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [str()] * (N)  # type: "List[str]"
    t = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        s[i] = next(tokens)
        t[i] = int(next(tokens))
    X = next(tokens)  # type: str
    solve(N, s, t, X)

if __name__ == '__main__':
    main()
