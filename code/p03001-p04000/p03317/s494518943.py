#!/usr/bin/env python3
import sys
import math
def solve(N: int, K: int, A: "List[int]"):
    # 最小値は絶対1になる
    cur = K
    answer = 1 + math.ceil((N-K)/(K-1))
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
