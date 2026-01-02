#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int, H: "List[int]"):

    H[0] = H[0]-1
    for i in range(1, N):
        if H[i-1]+1 == H[i]:
            H[i] -= 1
        elif H[i-1] == H[i]:
            H[i] = H[i]
        elif H[i-1] > H[i]:
            no()
            return
        else:
            H[i] -= 1
    yes()

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, H)


if __name__ == '__main__':
    main()
