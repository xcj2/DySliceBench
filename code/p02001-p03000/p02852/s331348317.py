#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, M: int, S: str):

    S = S[::-1]
    data = [0]*(N+1)
    past = 0
    for i in range(N+1):
        if S[i] == "1":
            data[i] = past
        else:
            past = i
    ans = []
    curr = 0
    while True:
        ne = curr+M
        if ne >= N:
            ans.append(N-curr)
            break
        if S[ne] == "1":
            ne = data[ne]
            if ne <= curr:
                print(-1)
                return
        ans.append(ne - curr)
        curr = ne
    print(*reversed(ans), sep=" ")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, M, S)


if __name__ == '__main__':
    main()
