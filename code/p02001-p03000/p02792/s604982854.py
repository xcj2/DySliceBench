#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

def solve(N: int):
    counts = [[0] * 10 for _ in range(10)]
    for i in range(10, N + 1):
        b = i % 10
        while i >= 10:
            i //= 10
        counts[i][b] += 1
    ret = 0
    for i in range(1, min(N + 1, 10)):
        ret += 1
        if counts[i][i] > 0:
            ret += counts[i][i] * 2
    for i in range(1, 10):
        for j in range(1, 10):
            ret += counts[i][j] * counts[j][i]
    print(ret)
    return

def solve_(N: int):
    def is_valid(n, a, b):
        if n % 10 != b:
            return False
        while n >= 10:
            n //= 10
        if n % 10 == a:
            return True
        return False
    ret = 0
    for i in range(1, 10):
        for x in range(1, N + 1):
            if is_valid(x, i, i):
                print(x, i, i)
                ret += 1
    print(' -------- ')
    for i in range(1, 10):
        for j in range(1, 10):
            for x in range(10, N + 1):
                if is_valid(x, i, j):
                    print(x, i, j)
                    ret += 1
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
