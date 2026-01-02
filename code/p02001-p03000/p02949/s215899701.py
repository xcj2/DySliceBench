#####コピペ
def BellmanFord(edges, num_v, source):
    # グラフの初期化
    inf = float("inf")
    dist = [-inf for i in range(num_v)]
    dist[source - 1] = 0

    # 辺の緩和
    buf = 0
    for i in range(num_v * 2):
        for edge in edges:
            if dist[edge[1] - 1] < dist[edge[0] - 1] + edge[2]:
                dist[edge[1] - 1] = dist[edge[0] - 1] + edge[2]
                if i >= num_v:
                    dist[edge[1] - 1] = inf
        if i == num_v - 1:
            buf = dist[-1]
    if dist[-1] != buf or dist[-1] == -inf:
        return -1
    return max(dist[-1], 0)
##########################################################################
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = []

N, M, P = LI()
cou = int(0)
maxC = 10000
d = [[float("inf") for i in range(N)] for i in range(N)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
V = []*M
for i in range(M):
    a, b, c = list(map(int,input().split()))
    V.append((a,b,c-P))
print(BellmanFord(V, N, 1))

#print(ans)
