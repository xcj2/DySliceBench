#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    A.sort(reverse=True)
    i = 0
    tmp = []
    while i < N- 1:
        if A[i] == A[i + 1]:
            tmp.append(A[i])
            i += 1
        i += 1
    if len(tmp) > 1:
        ret = tmp[0] * tmp[1]
    else:
        ret = 0
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
