#!/usr/bin/env python3
import sys

def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

def accum(s):
    value = 1
    for ss in s:
        value = value*ss
    return value

def solve(N: int):
    divisors = divisor(N)
    divisors.sort()
    answer = 10**12
    LEN = len(divisors)
    for i in range(0,LEN):
        seki = divisors[i]+divisors[LEN-1-i]
        answer = min(answer,seki)

    print(answer-2)
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
