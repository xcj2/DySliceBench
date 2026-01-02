#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(S: str):
    N = len(S)
    zeros = [0]*N
    nodes = zeros[:]
    for i in range(N):
        if S[i] == "R":
            nodes[i] = i+1
        else:
            nodes[i] = i-1
    buf = zeros[:]
    for _ in range(100):
        buf[:] = zeros
        for i in range(N):
            buf[i] = nodes[nodes[i]]
        nodes[:] = buf

    ans = zeros[:]
    for i in range(N):
        ans[nodes[i]] += 1

    print(*ans, sep=" ")

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
