#!/usr/bin/env python3
import sys


def solve(a: int, b: int, x: int):
    # N以下のxで割れる個数をもとめたい
    def counter(n):
        return n//x
    
    if a == 0:
        print(counter(b)+1)
        return 
    
    print(counter(b)-counter(a-1))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    solve(a, b, x)

if __name__ == '__main__':
    main()
