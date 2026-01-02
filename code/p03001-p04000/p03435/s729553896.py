#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(c: "List[List[int]]"):
    if (c[0][1] - c[0][0] == c[1][1] - c[1][0] and
        c[0][1] - c[0][0] == c[2][1] - c[2][0] and
        c[0][2] - c[0][1] == c[1][2] - c[1][1] and
        c[0][2] - c[0][1] == c[2][2] - c[2][1] and
        c[1][0] - c[0][0] == c[1][1] - c[0][1] and
        c[2][0] - c[1][0] == c[2][1] - c[1][1]):
        ret = YES
    else:
        ret = NO
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    c = [ [ int(next(tokens)) for _ in range(3) ] for _ in range(3) ]  # type: "List[List[int]]"
    solve(c)

if __name__ == '__main__':
    main()
