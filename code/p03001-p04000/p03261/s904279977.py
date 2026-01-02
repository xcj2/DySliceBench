#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, W: "List[str]"):
    used = set()
    used.add(W[0])
    ret = YES
    for i in range(1, N):
        if W[i][0] != W[i - 1][-1] or W[i] in used:
            ret = NO
            break
        used.add(W[i])
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [ next(tokens) for _ in range(N) ]  # type: "List[str]"
    solve(N, W)

if __name__ == '__main__':
    main()
