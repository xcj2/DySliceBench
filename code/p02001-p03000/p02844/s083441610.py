#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    counter = 0
    for i in range(1000):
        c = i % 10
        b = (i // 10) % 10
        a = (i // 100) % 10
        aa = S.find(str(a))
        if aa != -1 and aa < N - 2:
            bb = S[aa+1:].find(str(b))
            if bb != -1 and bb < N - 1:
                cc = S[aa+bb+2:].find(str(c))
                if cc != -1:
                    counter += 1
    print(counter)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: int
    solve(N, S)


if __name__ == '__main__':
    main()
