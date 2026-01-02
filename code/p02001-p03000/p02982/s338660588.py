#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, D: int, X: "List[List[int]]"):
    ret = 0
    for i in range(N):
        for j in range(i + 1, N):
            tmp = 0
            for k in range(D):
                tmp += (X[i][k] - X[j][k]) ** 2
            if tmp == int(tmp ** 0.5) * int(tmp ** 0.5):
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
    D = int(next(tokens))  # type: int
    X = [ [ int(next(tokens)) for _ in range(D) ] for _ in range(N) ]  # type: "List[List[int]]"
    solve(N, D, X)

if __name__ == '__main__':
    main()
