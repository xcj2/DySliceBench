#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(s: str):
    ans = []
    for c in s:
        if c == "B":
            if len(ans) > 0:
                ans.pop()
        else:
            ans.append(c)
    if len(ans) == 0:
        print("error")
    else:
        print("".join(ans))
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
