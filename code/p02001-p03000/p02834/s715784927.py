#!/usr/bin/env python3
import sys
from collections import deque

def solve(N: int, u: int, v: int, A: "List[int]", B: "List[int]"):
    matrix = [[] for _ in range(N+1)]
    for i in range(N-1):
        matrix[A[i]].append(B[i])
        matrix[B[i]].append(A[i])

    takahashi_dist = [-1]*(N+1)
    aoki_dist = [-1]*(N+1)

    queue_takahashi = deque([(u,0)])

    while queue_takahashi:
        node,dist = queue_takahashi.popleft()
        takahashi_dist[node] = dist

        for nd in matrix[node]:
            if takahashi_dist[nd] == -1:
                queue_takahashi.append((nd,dist+1))
    

    queue_aoki = deque([(v,0)])
    while queue_aoki:
        node,dist = queue_aoki.popleft()
        aoki_dist[node] = dist

        for nd in matrix[node]:
            if aoki_dist[nd] == -1:
                queue_aoki.append((nd,dist+1))

    answer = 0
    for j in range(1,N+1):
        if aoki_dist[j] > takahashi_dist[j]:
            answer = max(answer,aoki_dist[j]-1)
    print(answer)

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
