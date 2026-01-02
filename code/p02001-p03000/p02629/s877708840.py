#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int):
    ret = []
    while N > 0:
        tmp = N % 26
        if tmp > 0:
            ret.append(chr(ord('a') + tmp - 1))
        else:
            ret.append('z')
        N = (N - 1) // 26
    ret.reverse()
    ret = ''.join(ret)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
