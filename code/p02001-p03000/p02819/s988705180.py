#!/usr/bin/env python3
import sys


def solve(X: int):
    def is_prime(n):
        for i in range(2, n + 1):
            if i * i > n:
                break
            if n % i == 0:
                return False
        return n != 1


    while True:
        if is_prime(X):
            break
        X += 1
    print(X)

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
