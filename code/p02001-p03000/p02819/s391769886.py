#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def solve(X: int):
    while True:
        if is_prime(X):
            ret = X
            break
        X += 1
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
