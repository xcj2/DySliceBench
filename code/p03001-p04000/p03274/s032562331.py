#!/usr/bin/env python3
import sys


def solve(N: int, K: int, x: "List[int]"):
    def search(N, window_size, x):
        costs = []
        for i in range(N-window_size+1):
            right_end = x[i+window_size-1]
            left_end = x[i]
            dist = abs(right_end-left_end)
            costs.append(min(abs(right_end)+dist, abs(left_end)+dist))
        return min(costs)
    print(search(N, K, x))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, x)

if __name__ == '__main__':
    main()
