#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", Q: int, K: int, x: "List[int]", y: "List[int]"):

    """graph.input.linkedlist_with_weight
        input: u[]:start, v[]:end, w[]:weight
        output:g[][]
    """
    g = [[] for i in range(N+1)]
    for i in range(N-1):
        g[a[i]].append([b[i], c[i]])
        g[b[i]].append([a[i], c[i]])

    def dikstra(nodes: int, graph: "List[List[int, int]]", start: int):
        """dikstra
        
        Arguments:
            nodes {int} -- Nodes in graph
            graph {List["List[int, int]"]} -- graph (adjancency matrix)
            start {int} -- start point
        
        Returns:
            [type] -- great distances from start point to each nodes in graph
        """
        INF = 1<<48
        from heapq import heapify, heappop, heappush
        hq = []
        heapify(hq)
        # i-indexed
        colors = ['W'] * (nodes+1)
        d = [INF] * (nodes+1)
        d[start] = 0
    
        heappush(hq, [start, start])
        colors[start] = 'G'
    
        while hq:
            f = hq.pop()
            u = f[1]
            colors[u]= 'B'
            
            if d[u] < -f[0]:
                continue
    
            for adj_i in graph[u]:
                v = adj_i[0]
                if colors[v] == 'B':
                    continue
                if d[v] > d[u] + adj_i[1]:
                    d[v] = d[u] + adj_i[1]
                    heappush(hq, [-d[v], v])
                    colors[v] = 'G'
        return d
    
    d = dikstra(N, g, K)

    for i in range(Q):
        print(d[x[i]]+d[y[i]])

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
