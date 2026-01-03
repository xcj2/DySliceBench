#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(a: int, b: int):
    if a < 0 and b < 0:
        if (abs(a)-abs(b)+1)%2 == 0:
            print("Positive")
        else:
            print("Negative")
    
    elif a > 0 and b > 0:
        print("Positive")

    else:
        print("Zero")

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(a, b)

if __name__ == '__main__':
    main()
