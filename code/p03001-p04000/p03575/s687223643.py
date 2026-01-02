#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

def dfs(s, t, conn, visited):
    #print(s, t, visited)
    #print(s, t, conn)
    if s == t:
        return True
    visited[s] = True
    for n in conn[s]:
        if not visited[n] and dfs(n, t, conn, visited):
            return True
    return False


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    #conn = [[False] * N for _ in range(N)]
    ret = 0
    for i in range(M):
        conn = [[] for _ in range(N)]
        for j in range(M):
            if i == j:
                continue
            conn[a[j] - 1].append(b[j] - 1)
            conn[b[j] - 1].append(a[j] - 1)
        visited = [False] * N
        if not dfs(a[i] - 1, b[i] - 1, conn, visited):
            #print(a[i] - 1, b[i] - 1)
            #print()
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
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]" 
    b = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)

if __name__ == '__main__':
    main()
