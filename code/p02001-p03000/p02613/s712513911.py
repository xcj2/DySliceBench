#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, S: "List[str]"):
    s = {'AC': 0, 'WA': 0, 'TLE':0, 'RE':0}
    for c in S:
        s[c] += 1
    for c in ['AC', 'WA', 'TLE', 'RE']:
        print('{} x {}'.format(c, s[c]))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
