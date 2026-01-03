#!/usr/bin/env python3
import sys


def solve(N: int, M: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    for i in range(N):
        min_dist = 10**9
        min_index = None
        for j in range(M):
            dist = abs(a[i]-c[j])+abs(b[i]-d[j])
            if dist < min_dist:
                min_dist = dist
                min_index = j
        
        print(min_index+1)


    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [int()] * (M)  # type: "List[int]"
    d = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, M, a, b, c, d)

if __name__ == '__main__':
    main()
