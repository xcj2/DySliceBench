#!/usr/bin/env python3
import sys


def solve(N: int):
    cur = N
    ret = []
    i = 0
    if N == 0:
        ret = ['0']
    while abs(cur) > 0:
        if i % 2 == 0:
            elm = (2 ** i)
        else:
            elm = -(2 ** i)
        tmp =  2 ** (i + 1)
        #print(cur, elm, tmp)
        if abs(cur - elm) % tmp == 0:
            ret.append('1')
            cur -= elm
        else:
            ret.append('0')
        i += 1
    ret.reverse()
    print(''.join(ret))
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
