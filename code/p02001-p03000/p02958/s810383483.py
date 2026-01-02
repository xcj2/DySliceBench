#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("YES")  # type: str


def no():
    print("NO")  # type: str


def solve(N: int, p: "List[int]"):
    B = sorted(p)
    count = 0
    for bb, pp in zip(B, p):
        if bb != pp:
            count += 1
    if count <= 2:
        yes()
    else:
        no()

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)


if __name__ == '__main__':
    main()
