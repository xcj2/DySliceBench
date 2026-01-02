#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
def solve(N: int, Q: int, a: "List[int]", b: "List[int]", p: "List[int]", x: "List[int]"):
    answer = [0]*N
    linked_list = [[] for _ in range(N)]
    for i in range(N-1):
        linked_list[a[i]-1].append(b[i]-1)
        linked_list[b[i]-1].append(a[i]-1)
    
    c = [0]*N
    is_Visited = [False]*N

    for j in range(Q):
        c[p[j]-1] += x[j]
    answer[0] = c[0]
    
    def dfs(node,counter):
        counter += c[node]
        is_Visited[node] = True
        for n in linked_list[node]:
            if is_Visited[n] == False:
                answer[n] = dfs(n,counter)
        
        return counter
        
    dfs(0,0)
    print(*answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, Q, a, b, p, x)

if __name__ == '__main__':
    main()
