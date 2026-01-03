#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, S: str):
    ret = 0
    cur = 0
    for c in S:
        if c == 'I':
            cur += 1
            ret = max(ret, cur)
        else:
            cur -= 1
    print(ret)
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
