#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(a: int, b: int):
    n = int(str(a) + str(b))
    if int(n ** 0.5) * int(n ** 0.5) == n:
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
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(a, b)

if __name__ == '__main__':
    main()
