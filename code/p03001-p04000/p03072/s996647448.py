#!/usr/bin/env python3
import sys


def solve(N: int, H: "List[int]"):
    ret = 0
    for i in range(N):
        no = False
        for j in range(0, i):
            if H[i] < H[j]:
                no = True
                break
        if not no:
            ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, H)

if __name__ == '__main__':
    main()
