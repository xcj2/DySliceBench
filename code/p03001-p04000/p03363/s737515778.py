#!/usr/bin/env python3
import sys
from itertools import accumulate
from collections import Counter
from math import factorial
def comb(n, k):
    if n < k:
        return 0  
    k = min(n-k,k)
    ans = 1
    for i in range(1, k + 1):
        ans = (ans * (n + 1 - i) // i)
    return ans

def solve(N: int, A: "List[int]"):
    accum = accumulate(A)
    counter = dict(Counter(accum))

    answer = 0
    for key,value in counter.items():
        if key == 0:
            answer += value + comb(value,2)
        else:
            answer += comb(value,2)
    print(answer)
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
