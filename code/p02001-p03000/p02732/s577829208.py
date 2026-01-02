#!/usr/bin/env python3
import sys
from collections import Counter

def comb(n, k):
    if n <= 1:
        return 0
    ans = 1
    for i in range(1, k + 1):
        ans = (ans * (n + 1 - i) // i)
    return ans

def solve(N: int, A: "List[int]"):
    counter = dict(Counter(A))

    MAX = 0
    for _,value in counter.items():
        MAX += comb(value,2)

    for i in range(N):
        value = counter[A[i]]

        print(MAX-comb(value,2)+comb(value-1,2))



    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
