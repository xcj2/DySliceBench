#!/usr/bin/env python3
import sys


def solve(N: int, P: int):
        ## 約数の列挙O(√N)
    def divisor(n): #nの約数を全て求める
        i = 1
        table = []
        while i * i <= n:
            if n%i == 0:
                table.append(i)
                table.append(n//i)
            i += 1
        table = sorted(list(set(table)))
        return table

    divisors = divisor(P)

    answer = 1
    if N > 40:
        print(answer)
        return 
    for div in divisors:
        if div**N > P:
            break

        if P%(div**N) == 0:
            answer = div

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(N, P)

if __name__ == '__main__':
    main()
