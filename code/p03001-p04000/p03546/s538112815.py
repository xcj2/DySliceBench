#!/usr/bin/env python3
import sys

def warshall_floyd(d, V): 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d #d[i][j]に頂点i, j間の最短距離を格納

def solve(H: int, W: int, c: "List[List[int]]", A: "List[List[int]]"):
    min_cost = warshall_floyd(c,10)
    answer = 0

    for h in range(H):
        for w in range(W):
            if A[h][w] == -1:
                continue

            answer += min_cost[A[h][w]][1]
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    c = [[int(next(tokens)) for _ in range(9 - 0 + 1)] for _ in range(9 - 0 + 1)]  # type: "List[List[int]]"
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, c, A)

if __name__ == '__main__':
    main()
