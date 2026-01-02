#!/usr/bin/env python3
import sys


def solve(n: int, h: "List[int]"):
    ret = 0
    while True:
        tmp = 0
        found = False
        for i in range(n):
            if h[i] > 0:
                h[i] -= 1
                if not found:
                    found = True
                    tmp += 1
            else:
                found = False
        if tmp < 1:
            break
        else:
            ret += tmp
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, h)

if __name__ == '__main__':
    main()
