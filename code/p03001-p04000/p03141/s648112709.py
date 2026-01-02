#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    tmp = []
    for i in range(N):
        tmp.append([A[i], B[i], A[i] + B[i]])
    tmp.sort(reverse=True, key=lambda x: x[2])
    ret = 0
    for i in range(N):
        t = tmp[i][0] if i % 2 == 0 else -tmp[i][1]
        ret += t
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]" 
    B = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
