#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]"):
    ret = 0
    a = 0
    b = 0
    ab = 0
    for s in S:
        i = 0
        for i in range(len(s) - 1):
            if s[i:i+2] == 'AB':
                ret += 1
        if s[0] == 'B':
            a += 1
        if s[-1] == 'A':
            b += 1
        if s[0] == 'B' and s[-1] == 'A':
            ab += 1
    ret += min(a, b)
    if a > 0 and a == b and a == ab:
        ret -= 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [ next(tokens) for _ in range(N) ]  # type: "List[str]"
    solve(N, s)

if __name__ == '__main__':
    main()
