#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(O: str, E: str):
    ret = [None] * (len(O) + len(E))
    for i in range(len(O)):
        ret[i * 2] = O[i]
    for i in range(len(E)):
        ret[i * 2 + 1] = E[i]
    print(''.join(ret))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    O = next(tokens)  # type: str
    E = next(tokens)  # type: str
    solve(O, E)

if __name__ == '__main__':
    main()
