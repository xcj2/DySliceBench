#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, H: "List[int]"):
    ret = 0
    tmp = 0
    for i in range(1, N):
        if H[i] <= H[i - 1]:
            tmp += 1
            ret = max(ret, tmp)
        else:
            tmp = 0
    ret = max(ret, tmp)
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
