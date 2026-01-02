# ABC168d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))
    from collections import deque
    INF = 10**12

    import heapq
    import sys

    input = sys.stdin.readline

    def dijkstra_heap(s, edge, n):
        # 始点sから各頂点への最短距離
        d = [INF] * n
        used = [True] * n  # True:未確定
        d[s] = 0
        used[s] = False
        edgelist = []
        frm = [-1]*n
        for a, b in edge[s]:
            heapq.heappush(edgelist, (a*(10**6)+b, -1))
        while len(edgelist):
            minedge = heapq.heappop(edgelist)
            froom = minedge[1]
            minedge = minedge[0]
            # まだ使われてない頂点の中から最小の距離のものを探す
            if not used[minedge % (10**6)]:
                continue
            v = minedge % (10**6)
            d[v] = minedge // (10 ** 6)
            frm[v] = froom
            used[v] = False
            for e in edge[v]:
                if used[e[1]]:
                    heapq.heappush(edgelist, ((e[0]+d[v])*(10**6)+e[1], v))
        return (d, frm)

    n, m = map(int, input().split())
    edges = [list() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a - 1].append((1, b - 1))
        edges[b - 1].append((1, a - 1))

    dist = dijkstra_heap(0, edges, n)
    #print(dist[0], dist[1])
   # print(graph.dist)
    # print(graph.frm)
    if INF in dist[0]:
        print('No')
        exit(0)
    print('Yes')
    for i in dist[1][1:]:
        print(i+1 if i+1 != 0 else 1)


if __name__ == '__main__':
    main()
