#!/usr/bin/env python3
import sys
import math
## 組み合わせの総数だけ知りたい
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def solve(N: int, M: int):
    answer = 0
    if N >= 2:
        answer += comb(N,2)
    
    if M >= 2:
        answer += comb(M,2)

    print(answer)

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
