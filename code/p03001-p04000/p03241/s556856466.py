#!/usr/bin/env python3
import sys
from bisect import bisect_left


## 約数の列挙O(N)
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

def solve(N: int, M: int):
    if M%N == 0:
        print(M//N)
        return

    max_answer = M//N
    divisors = divisor(M)
    divisors.sort()

    index = bisect_left(divisors,max_answer)
    if index == 0:
        print(1)
        return 
    print(divisors[index-1])


    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
