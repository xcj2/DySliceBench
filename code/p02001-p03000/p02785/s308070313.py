#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().strip()

def solve(N: int, K: int, H: "List[int]"):
    H.sort()
    print(sum(H[i] for i in range(N - K)) if K < N else 0)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, H)

if __name__ == '__main__':
    main()
