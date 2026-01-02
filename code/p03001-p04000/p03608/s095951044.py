#!/usr/bin/env python3
import sys
from itertools import permutations
 
def warshall_floyd(conn):
    n = len(conn)
    dp = [[v for v in A] for A in conn]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp
 
 
def solve(N: int, M: int, R: int, r: "List[int]", A: "List[int]", B: "List[int]", C: "List[int]"):
    conn = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        conn[i][i] = 0
    for j in range(M):
        a = A[j] - 1
        b = B[j] - 1
        conn[a][b] = min(conn[a][b], C[j])
        conn[b][a] = min(conn[b][a], C[j])
    dp = warshall_floyd(conn)
    #print(dp)
    ret = float('inf')
    perms = list(permutations(list(range(R))))
    for order in perms:
        tmp = 0
        for i in range(R - 1):
            s = r[order[i]] - 1
            t = r[order[i + 1]] - 1
            #print(r[s], r[t], dp[s][t])
            tmp += dp[s][t]
        ret = min(ret, tmp)
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
    R = int(next(tokens))  # type: int
    r = [ int(next(tokens)) for _ in range(R) ]  # type: "List[int]"
    A = [int()] * (M)  # type: "List[int]" 
    B = [int()] * (M)  # type: "List[int]" 
    C = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, R, r, A, B, C)
 
if __name__ == '__main__':
    main()