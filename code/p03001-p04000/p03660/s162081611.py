import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    # https://atcoder.jp/contests/abc070/tasks/abc070_d
    # https://atcoder.jp/contests/abc070/submissions/11681543
    from heapq import heapify, heappop, heappush

    inf = 10 ** 17

    def dijkstra_heap(start, edge):
        # 始点から各頂点への最短距離(頂点番号:0~N-1)
        d = [inf] * N
        used = [False] * N
        d[start] = 0
        used[start] = True
        edgelist = []
        # a:重み(//), b:次の頂点(%)
        for a, b in edge[start]:
            heappush(edgelist, a * (10 ** 6) + b)

        while len(edgelist):
            # まだ最短距離が決まっていない頂点の中から最小の距離のものを探す
            minedge = heappop(edgelist)
            if used[minedge % (10 ** 6)]:
                continue
            node = minedge % (10 ** 6)
            d[node] = minedge // (10 ** 6)
            used[node] = True

            for e in edge[node]:
                if not used[e[1]]:
                    heappush(edgelist, (e[0] + d[node]) * (10 ** 6) + e[1])
        return d

    # N:頂点数 W:辺数
    N = int(input())
    W = N-1

    edge = [[] for i in range(N)]
    # edge[i] : iから出る道の[重み,行先]の配列
    for _ in range(W):
        x, y = map(int, input().split())
        edge[x - 1].append((1, y - 1))
        edge[y - 1].append((1, x - 1))

    fen = dijkstra_heap(0, edge)
    sun = dijkstra_heap(N-1, edge)
    f = 0
    s = 0

    for i in range(1, N-1):
        if fen[i] <= sun[i]:
            f += 1
        elif fen[i] > sun[i]:
            s += 1
    print('Fennec' if f > s else 'Snuke')


resolve()