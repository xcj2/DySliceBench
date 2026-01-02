#!/usr/bin/env python3
import sys

YES = 'Yay!'
NO =  ':('

def solve(a: int, b: int, c: int, d: int, e: int, k: int):
    if (b - a > k or c - b > k or d - c > k or e - d > k or 
       c - a > k or d - b > k or e - c > k or d > k or
       d - a > k or e - b > k or e - a > k):
        ret = NO
    else:
        ret = YES
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    e = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(a, b, c, d, e, k)

if __name__ == '__main__':
    main()
