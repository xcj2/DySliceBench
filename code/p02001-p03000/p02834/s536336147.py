#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, u: int, v: int, A: "List[int]", B: "List[int]"):
    u -= 1
    v -= 1
    conns = [[] for _ in range(N)]
    for j in range(N - 1):
        conns[A[j] - 1].append(B[j] - 1)
        conns[B[j] - 1].append(A[j] - 1)

    def dfs(idx, cur, dis):
        dis[idx] = cur
        for conn in conns[idx]:
            if dis[conn] < 0:
                dis = dfs(conn, cur + 1, dis)
        return dis

    dis_u = [-1] * N
    dis_u = dfs(u, 0, dis_u)
    dis_v = [-1] * N
    dis_v = dfs(v, 0, dis_v)
    ret = 0
    for i in range(N):
        if dis_u[i] < dis_v[i]:
            ret = max(ret, dis_u[i] + (dis_v[i] - dis_u[i] - 1))
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = int(next(tokens))  # type: int
    v = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, u, v, A, B)

if __name__ == '__main__':
    main()
