#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: "List[int]"):
    A = [0] + A + [0]

    forward = [0]
    curr = 0
    for i in range(N+1):
        forward.append(forward[-1] + abs(curr-A[i+1]))
        curr = A[i+1]

    backward = [0]
    curr = 0
    for i in range(N+1):
        backward.append(backward[-1] + abs(curr-A[N-i]))
        curr = A[N-i]
    backward = backward[::-1]

    buf = []
    for i in range(1, N+1):
        print(forward[i-1] + backward[i+1] + abs(A[i-1] - A[i+1]))

    # print(forward)
    # print(backward)

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
