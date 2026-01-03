#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, a: "List[int]"):
    visited = [False]*N
    curr = 1
    counter = 0
    while curr != 2:
        if visited[curr-1]:
            print(-1)
            return
        visited[curr-1] = True
        curr = a[curr-1]
        counter += 1
    print(counter)

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
