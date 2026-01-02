#!/usr/bin/env python3
import sys


def solve(N: int, K: int, h: "List[int]"):
    h.sort(reverse=True)
    count = 0

    for member_cm in h:
        if member_cm >= K:
            count += 1
        else:
            pass
        if member_cm < K:
            break
        else:
            pass
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)


if __name__ == "__main__":
    main()
