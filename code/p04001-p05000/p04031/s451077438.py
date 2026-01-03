#!/usr/bin/env python3
import sys

def solve(N: int, a: "List[int]"):
    min_cost = 10**9

    for target in range(-100,101):
        tmp = 0
        for i in range(N):
            tmp += (a[i]-target)**2
        min_cost = min(min_cost,tmp)
    print(min_cost)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
