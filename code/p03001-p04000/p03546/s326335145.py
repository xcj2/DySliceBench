#  --*-coding:utf-8-*--

import heapq

INF = float("inf")

def dijkstra(graph, st):
    n  = len(graph)
    ds = [INF]*n
    ds[st] = 0
    prevs = [None]*n
    
    qs = [(0, st)]

    while len(qs) > 0:
        d, nodeId = heapq.heappop(qs)
        
        if d > ds[nodeId]:
            continue
        
        for destId, length in graph[nodeId]:
            d2 = d + length
            if ds[destId] > d2:
                ds[destId] = d2
                prevs[destId] = nodeId
                heapq.heappush(qs, (d2, destId))
                
    return (ds, prevs)


def f(H, W, C, A):
    graph = [[(i, C[i][j]) for i in range(10)] for j in range(10)]
    ds, _ = dijkstra(graph, 1)

    return sum(ds[a] if a>= 0 else 0 for line in A for a in line)

    
def main():
    H,W = map(int, input().split())
    C = [list(map(int, input().split())) for i in range(10)]
    A = [list(map(int, input().split())) for i in range(H)]

    print(f(H,W,C,A))


if __name__ == '__main__':
    main()
