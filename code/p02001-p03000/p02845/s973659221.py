#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    RGB = [-1, -1, -1]
    ans = 1
    for a in A:
        count = 0
        for i in range(3):
            if RGB[i] == a-1:
                if count == 0:
                    RGB[i] = a
                count += 1
        if count > 1:
            ans *= count
            ans %= MOD
        elif count == 0:
            ans = 0
            print(ans)
            return
    print(ans)

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
