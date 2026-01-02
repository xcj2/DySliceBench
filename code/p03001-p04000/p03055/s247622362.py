#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

def dfs(idx, con, visited):
    visited[idx] = True
    max_depth = 0
    max_len = 0
    depths = []
    if idx >= len(con):
        return max_depth, max_len
    for v in con[idx]:
        if v < len(visited) and not visited[v]:
            max_d, max_l = dfs(v, con, visited)
            max_len = max(max_len, max_l)
            depths.append(max_d + 1)
    if len(depths) > 0:
        depths.sort(reverse=True)
        max_depth = depths[0]
        if len(depths) > 1:
            max_len = max(max_len, depths[0] + depths[1])
        else:
            max_len = max(max_len, depths[0])
    visited[idx] = False
    return max_depth, max_len


def solve(N: int, A: "List[int]", B: "List[int]"):
    con = [[] for _ in range(N)]
    for i in range(len(A)):
        a = A[i] - 1
        b = B[i] - 1
        con[a].append(b)
        con[b].append(a)
    #print(con)
    visited = [False] * N
    max_depth, max_len = dfs(0, con, visited)
    #print(max_len)
    if (max_len + 1) % 3 == 2:
        ret = 'Second'
    else:
        ret = 'First'
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N-1)  # type: "List[int]" 
    b = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

if __name__ == '__main__':
    main()
