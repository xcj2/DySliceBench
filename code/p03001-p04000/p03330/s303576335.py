#!/usr/bin/env python3
import sys
import itertools 

def solve(N: int, C: int, D: "List[List[int]]", c: "List[List[int]]"):
    answer = 10**9

    cost = [[0 for _ in range(C)] for _ in range(3)]


    for i in range(1,N+1):
        for j  in range(1,N+1):
            cost[(i+j)%3][c[i-1][j-1]-1] += 1

    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i==j or j==k or k==i:
                    continue
                a = 0
                for index in range(C):
                    a += cost[0][index]*D[index][i]
                    a += cost[1][index]*D[index][j]
                    a += cost[2][index]*D[index][k]
                
                answer = min(a,answer)

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(C)] for _ in range(C)]  # type: "List[List[int]]"
    c = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, C, D, c)

if __name__ == '__main__':
    main()
