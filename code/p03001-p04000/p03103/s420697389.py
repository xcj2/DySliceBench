#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    pairs = []
    for i in range(N):
        pairs.append((A[i], B[i]))
    pairs.sort(key=lambda x: x[0])
    ret = 0
    for p, num in pairs:
        if M <= num:
            ret += p * M
            break
        else:
            ret += p * num
            M -= num
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]" 
    B = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
