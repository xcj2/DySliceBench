#!/usr/bin/env python3
import sys
import math

def solve(A: int, B: int):
    ten = B * 10
    ans = int(ten)

    while True:
        if ans // 10 != B :
            print(-1)
            return
        elif math.floor(ans * 0.08) == A:
            print(ans)
            return
        ans += 1

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
