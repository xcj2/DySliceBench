import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30
from collections import Counter

W = 0
def g_i(i, j):
    return i * W + (j+1) - 1

def dijkstra(n, start, nbl):
    """n: 頂点数, start: 始点, nbl: 隣接リスト"""
    import heapq
    WHITE = 1<<5
    GRAY = 1<<10
    BLACK = 1<<15
    color = [WHITE] * n
    distance = [INF] * n
    parent = [-1] * n
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))
    while len(q) != 0:
        du, u = heapq.heappop(q)
        # print("u: {}, du: {}".format(u, du))
        color[u] = BLACK
        if distance[u] < du:
            continue
        for next, cost in nbl[u]:
            if color[next] != BLACK and distance[u] + cost < distance[next]:
                distance[next] = distance[u] + cost
                parent[next] = u
                color[next] = GRAY
                heapq.heappush(q, (distance[next], next))
    return (distance, parent)

def main():
    global W
    h, W = map(int, input().strip().split())
    w = W
    s = [[0] * w for _ in range(h)]
    G = [[] for _ in range(h * w)]
    for i in range(h):
        s[i] = list(input().strip())
    sc = 0
    dc = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                sc += 1
                continue
            dc += 1
            if i != 0 and s[i-1][j] == '.':
                G[g_i(i, j)].append((g_i(i-1, j), 1))
            if i != h-1 and s[i+1][j] == '.':
                G[g_i(i, j)].append((g_i(i+1, j), 1))
            if j != 0 and s[i][j-1] == '.':
                G[g_i(i, j)].append((g_i(i, j-1), 1))
            if j != w-1 and s[i][j+1] == '.':
                G[g_i(i, j)].append((g_i(i, j+1), 1))
    # print(G)
    d, p = dijkstra(h * w, 0, G)
    # print(d[h*w - 1])
    # for i in range(h):
    #     for j in range(w):
    #         if p[g_i(i, j)] != -1:
    #             print('.', end='')
    #         else:
    #             print('#', end='')
    #     print('\n', end='')
    # print(g_i(h-1, w-2))
    # print(p[g_i(h-1, w-2)])
    # print(p)
    if d[h*w - 1] == INF:
        print(-1)
    else:
        print(dc - d[h*w - 1] - 1)

if __name__ == '__main__':
    main()
