#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, a: "List[int]"):
    count = [0] * 3
    for v in a:
        if v % 4 == 0:
            count[2] += 1
        elif v % 2 == 0:
            count[1] += 1
        else:
            count[0] += 1
    if count[0] == count[2] + 1 and count[1] == 0:
        ret = YES
    elif count[0] > count[2]:
        ret = NO
    else:
        ret = YES
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
