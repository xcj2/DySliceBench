#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    conn = [[] * N for _ in range(N)]
    for i in range(M):
        conn[a[i] - 1].append(b[i] - 1)
        conn[b[i] - 1].append(a[i] - 1)
    def dfs(idx, visited):
        last = True
        for v in visited:
            if not v:
                last = False
                break
        if last:
            return 1
        ret = 0
        for nex in conn[idx]:
            if not visited[nex]:
                visited[nex] = True
                ret += dfs(nex, visited)
                visited[nex] = False
        return ret
    visited = [False] * N
    visited[0] = True
    count = dfs(0, visited)
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]" 
    b = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)

if __name__ == '__main__':
    main()
