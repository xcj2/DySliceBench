#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(s: str):

    ans = 0
    A = 0
    B = 0
    process = []
    for c in s:
        if c == "A":
            if B == 0:
                A += 1
            else:
                A = 1
                B = 0
        elif A > 0 and c == "B":
            if B == 0:
                B = 1
            else:
                B = 0
                A = 0
        elif A > 0 and B > 0 and c == "C":
            ans += A
            B = 0
        else:
            A = 0
            B = 0
    print(ans)
    # print(process)

    # counter = 0
    # while "ABC" in s:
    #     s = s.replace("ABC", "BCA", 1)
    #     # print(s)
    #     counter += 1
    # print(counter)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)


if __name__ == '__main__':
    main()
