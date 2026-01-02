#!/usr/bin/env python3
import sys
INF = float("inf")
import numpy as np
from collections import Counter
from itertools import permutations


def solve(N: int, C: int, D: "List[List[int]]", c: "List[List[int]]"):
    D = np.array(D)
    onedim = [[], [], []]
    for i in range(N):          # O(N^2)
        for j in range(N):
            onedim[(i+j) % 3].append(c[i][j])
    # print(onedim)
    counters = [Counter(onedim[i]) for i in range(3)]  # O(3*N*N)
    arr = np.empty((C, C))
    for i in range(3):          # O(C*C)
        for j in range(C):
            arr[i][j] = counters[i][j+1]
    # print("arr", arr)
    # print("D", D)
    hint = arr.dot(D)         # O(C*C*3)
    # print("arr@D\n", hint)
    print(int(min([hint[0][a] + hint[1][b]+hint[2][c]
                   for a, b, c in permutations(range(C), 3)])))
    # O(C*(C-1)*(C-2))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(C)]
         for _ in range(C)]  # type: "List[List[int]]"
    c = [[int(next(tokens)) for _ in range(N)]
         for _ in range(N)]  # type: "List[List[int]]"
    solve(N, C, D, c)


if __name__ == '__main__':
    main()
