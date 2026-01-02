#!/usr/bin/env python3
import sys


def solve(N: int, M: int, P: "List[int]", Y: "List[int]"):
    tmp = []
    for i in range(M):
        p = P[i]
        y = Y[i]
        tmp.append([i, p, y, ''])
    tmp.sort(key=lambda x: x[2])
    count = [0] * (N + 1)
    for t in tmp:
        p = t[1]
        count[p] += 1
        t[3] = '%06d%06d' % (p, count[p])
    tmp.sort(key=lambda x: x[0])
    for t in tmp:
        print(t[3])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = [int()] * (M)  # type: "List[int]" 
    Y = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        P[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, P, Y)

if __name__ == '__main__':
    main()
