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

    can = [True] * N
    def find_v(idx, dis, visited):
        visited[idx] = True
        if idx == v:
            can[idx] = False
            return (dis, -1)
        ret = 0
        target = -1
        for conn in conns[idx]:
            if not visited[conn]:
                ret, target = find_v(conn, dis + 1, visited)
                if ret > 0:
                    if dis >= ret / 2:
                        can[idx] = False
                    if dis < ret / 2 and target == -1:
                        target = idx
                    break
        return ret, target
    visited = [False] * N
    uv, node = find_v(u, 0, visited)
    #print(can)
    #print('uv: ', uv)
    #print('node: ', node)
    #print(' ---- ' )
    def dfs(idx, dis, visited):
        visited[idx] = True
        ret = dis
        for conn in conns[idx]:
            if not visited[conn] and can[conn]:
                tmp = dfs(conn, dis + 1, visited)
                ret = max(ret, tmp)
        return ret
    visited = [False] * N
    ret = dfs(node, 0, visited)
    #print('ret:', ret)
    ret += uv // 2
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
