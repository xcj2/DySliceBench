#!/usr/bin/env python3
import sys
from collections import deque

def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", Q: int, K: int, x: "List[int]", y: "List[int]"):
    matrix = dict()

    for i in range(N-1):
        if matrix.get(a[i]) == None:
            matrix[a[i]] = [(b[i],c[i])]
        else:
            matrix[a[i]].append((b[i],c[i]))

        if matrix.get(b[i]) == None:
            matrix[b[i]] = [(a[i],c[i])]
        else:
            matrix[b[i]].append((a[i],c[i]))

    # i = NodeKからnodeiまでの距離
    distance_via_K = [-1]*(N+1)

    queue = deque()
    ## K を頂点として見る
    queue.append((K,0))

    while queue:
        q,cur_distance = queue.pop()
        distance_via_K[q] = cur_distance

        for node,distance in matrix[q]:
            if distance_via_K[node] == -1:
                queue.append((node,cur_distance+distance))

    for j in range(Q):
        print(distance_via_K[x[j]]+distance_via_K[y[j]])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    c = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, a, b, c, Q, K, x, y)

if __name__ == '__main__':
    main()
