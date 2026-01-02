#!/usr/bin/env python3
import sys
import collections

def breadth_first_search(graph, root): 
    visited, queue = set([root]), collections.deque([root])
    color = [0] * len(graph)
    # root is always 0
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour[0] not in visited: 
                visited.add(neighbour[0]) 
                queue.append(neighbour[0])
                color[neighbour[0]] = (color[vertex] + neighbour[1] % 2) % 2
    return color 

def solve(N: int, u: "List[int]", v: "List[int]", w: "List[int]"):
    graph = [[] for i in range(N)]
    for i in range(len(u)):
        graph[u[i]-1] += [[v[i]-1, w[i]]]
        graph[v[i]-1] += [[u[i]-1, w[i]]]
    color = breadth_first_search(graph, 0)
    print("\n".join(list(map(str, color))))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    w = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, u, v, w)

if __name__ == '__main__':
    main()
