#!/usr/bin/env python3
import sys
from collections import deque

def solve(N: int, a: "List[int]", b: "List[int]"):
    h = [[] for _ in range(N+1)]    

    for i in range(N-1):
        h[a[i]].append(b[i])
        h[b[i]].append(a[i])

    queue = deque([1])

    ## 頂点iの親を格納
    parents = [0]*(N+1)
    order = []

    while queue:
        q = queue.pop()
        order.append(q)

        for child in h[q]:
            if child == parents[q]:
                continue

            parents[child] = q
            queue.append(child)

    ## 頂点i と親nodeの間のcolor
    color = [0]*(N+1)

    for o in order:
        ng_color = color[o]
        cur_color = 1

        for node in h[o]:
            if node == parents[o]:
                continue

            if cur_color == ng_color:
                cur_color += 1
            
            color[node] = cur_color
            cur_color += 1


    answer = []
    append = answer.append
    for i in range(N-1):
        if parents[a[i]] == b[i]:
            append(color[a[i]])
        else:
            append(color[b[i]])

    print(max(answer))
    print(*answer, sep="\n")

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
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

if __name__ == '__main__':
    main()
