#!/usr/bin/env python3
import sys
import math
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int, a: "List[int]"):
    odd, even, eveven = 0, 0, 0
    for av in a:
        b = int(math.log2(av & -av))
        if b == 0:
            odd += 1
        elif b == 1:
            even += 1
        else:
            eveven += 1
    if odd > int(math.ceil(N/2)):
        no()
    elif even > 0 and odd > eveven:
        no()
    elif even == 0 and odd <= eveven:
        yes()
    else:
        yes()

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
