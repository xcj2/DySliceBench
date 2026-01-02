#!/usr/bin/env python3
import sys


def solve(H: int, W: int, D: int, A: "List[List[int]]", Q: int, L: "List[int]", R: "List[int]"):
    N = H*W

    ## ある数字の座標をO(1)で取得するため
    matrix = [()]*(N+1)
    for h in range(H):
        for w in range(W):
            matrix[A[h][w]] = (h,w)
    
    def get_distance(start: int, end: int) -> int:
        start_x = matrix[start][0]
        start_y = matrix[start][1]
        end_x = matrix[end][0]
        end_y = matrix[end][1]
        return abs(start_x-end_x)+abs(start_y-end_y)

    distance = []

    for start in range(1,D+1):
        end = start
        ## 初期化
        distance_matrix = {}
        while end <= N:
            distance_matrix[end] = 0
            end += D

        end = start
        prev_end = end

        while end <= N:
            distance_matrix[end] = distance_matrix[prev_end]+ get_distance(prev_end,end)
            prev_end = end
            end += D
        
        distance.append(distance_matrix)
    
    for i in range(Q):
        s = L[i]%D
        if s == 0:
            s = D
        distance_matrix = distance[s-1]
        d = distance_matrix[R[i]]-distance_matrix[L[i]]
        print(d)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    Q = int(next(tokens))  # type: int
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(H, W, D, A, Q, L, R)

if __name__ == '__main__':
    main()
