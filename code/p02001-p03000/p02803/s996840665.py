import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

nei = []
ans = 0
color = []

def dfs(i, fr, hop):
    global nei, color, ans
    ans = max(ans, hop)
    color[i] = 1
    for k in nei[i]:
        if k != fr and color[k] == -1:
            dfs(k, i, hop+1)

def dijkstra(n, start, nbl):
    """n: 頂点数, start: 始点, nbl: 隣接リスト"""
    import heapq
    WHITE = 1<<5
    GRAY = 1<<10
    BLACK = 1<<15
    INF = 1<<20
    color = [WHITE] * n
    distance = [INF] * n
    # parent = [-1] * n
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
                color[next] = GRAY
                heapq.heappush(q, (distance[next], next))
    for i, v in enumerate(distance[:]):
        if v == INF:
            distance[i] = -1
    return distance

def main():
    global nei, color
    h, w = list(map(int, input().strip().split()))
    G = [0] * h
    nei = [[] for _ in range(w*h)]
    color = [-1] * (w*h)
    for i in range(h):
        G[i] = input().strip()
    for i in range(h):
        for j in range(w):
            if G[i][j] == '.':
                if i != 0 and G[i-1][j] == '.':
                    nei[w*i+j].append((w*(i-1)+j, 1))
                if i != h-1 and G[i+1][j] == '.':
                    nei[w*i+j].append((w*(i+1)+j, 1))
                if j != 0 and G[i][j-1] == '.':
                    nei[w*i+j].append((w*i+j-1, 1))
                if j != w-1 and G[i][j+1] == '.':
                    nei[w*i+j].append((w*i+j+1, 1))
    ans = 0
    for i in range(h):
        for j in range(w):
            if G[i][j] == '.':
                # print(dijkstra(w*h, w*i+j, nei))
                ans = max(max(dijkstra(w*h, w*i+j, nei)), ans)
    print(ans)

if __name__ == '__main__':
    main()
