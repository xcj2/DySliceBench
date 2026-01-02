#!/usr/bin/env python3
import sys
import itertools

def solve(N: int, M: int, x: "List[int]", y: "List[int]", z: "List[int]"):

    sign = list(itertools.product([1, -1], repeat=3))
    cand = []
    for sx, sy, sz in sign:
        sub_c = [sx*x+sy*y+sz*z for x, y, z in zip(x,y,z)]
        sub_c.sort(reverse=True)
        cand.append(sum(sub_c[:M]))
    print(max(cand))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    z = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        z[i] = int(next(tokens))
    solve(N, M, x, y, z)

if __name__ == '__main__':
    main()
