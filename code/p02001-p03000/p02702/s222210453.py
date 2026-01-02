#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(S: str):
    s = [0] * 2019
    s[0] = 1
    ret = 0
    for c in S:
        cc = int(c)
        n = [0] * 2019
        for k, v in enumerate(s):
            kk = (k * 10 + cc) % 2019
            n[kk] += v
            if kk == 0:
                ret += v
        s = n
        n[0] += 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()
