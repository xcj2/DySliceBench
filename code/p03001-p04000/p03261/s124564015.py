#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, W: "List[str]"):
    if N != len(set(W)):
        print(NO)
        exit()

    for i in range(1, len(W)):
        if W[i-1][-1] != W[i][0]:
            print(NO)
            exit()
    print(YES)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, W)


if __name__ == '__main__':
    main()
