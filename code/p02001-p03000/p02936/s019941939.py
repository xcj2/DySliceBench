#!/usr/bin/env python3
import sys
from collections import deque

def solve(N: int, Q: int, a: "List[int]", b: "List[int]", p: "List[int]", x: "List[int]"):
    matrix = [[] for _ in range(N+1)]
    counter = [0]*(N+1)
    for i in range(N-1):
        matrix[a[i]].append(b[i])
        matrix[b[i]].append(a[i])

    for q in range(Q):
        counter[p[q]]+=x[q]

    queue = deque()
    queue.append(1)

    checkflag = [False]*(N+1)
    while queue:
        root = queue.pop()
        checkflag[root]=True
        for node in matrix[root]:
            if checkflag[node] == False:
                queue.append(node)
                counter[node]+=counter[root]

    print(*counter[1:])




        
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
