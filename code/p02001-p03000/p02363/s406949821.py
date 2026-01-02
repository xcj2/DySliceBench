inf = float('inf')
# ベルマンフォード法 計算量(VE)
# [引数]: 隣接リスト, 始点, 終点
class Bellmanford:
    def __init__(self, to:list, start:int, goal:int = -1):
        self.N = len(to)
        self.to = [s[:] for s in to]
        self.start = start
        self.goal = goal
        self.dist = [inf] * self.N
        self.dist[start] = 0
        self.exists_negative_cycle = False
        self.exists_negative_cycle_stog = False
        self.is_updated = [False] * self.N

    # distを更新
    def update(self) -> None:
        for _ in range(self.N - 1):
            for v, s in enumerate(self.to):
                if not s: continue
                for nv, w in s:
                    if self.dist[nv] > self.dist[v] + w:
                        self.dist[nv] = self.dist[v] + w

    # グラフの負閉路検出
    def detection(self) -> bool:
        for v, s in enumerate(self.to):
            if not s: continue
            for nv, w in s:
                if self.dist[nv] > self.dist[v] + w:
                    self.dist[nv] = self.dist[v] + w
                    self.exists_negative_cycle = True
        return self.exists_negative_cycle

    # スタートからゴールまでのパスの負閉路検出
    def detection_stog(self) -> bool:
        for _ in range(self.N):
            for v, s in enumerate(self.to):
                if not s: continue
                for nv, w in s:
                    if self.dist[nv] > self.dist[v] + w:
                        self.dist[nv] = self.dist[v] + w
                        self.is_updated[nv] = True
                    if self.is_updated[v] is True:
                        self.is_updated[nv] = True
        self.exists_negative_cycle_stog = self.is_updated[self.goal]
        return self.exists_negative_cycle_stog

inf = float('inf')
# ワーシャルフロイド法 計算量O(N^3)
# [引数]: 隣接行列
class Warshallfloyd:
    def __init__(self, admat:list):
        self.N = len(admat)
        self.dist = [c[:] for c in admat]

    def update(self) -> None:
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    if i == j:
                        self.dist[i][j] = 0
                    elif self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]

N, M = map(int,input().split())
to = [[] for _ in range(N)]
admat = [[inf] * N for _ in range(N)]
for _ in range(M):
    s, t, d = map(int,input().split())
    to[s].append((t, d))
    admat[s][t] = d

BF = Bellmanford(to, 0)
BF.update()
if BF.detection():
    print("NEGATIVE CYCLE")
    exit()
WF = Warshallfloyd(admat)
WF.update()
ans_list = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        ans_list[i][j] = WF.dist[i][j] if WF.dist[i][j] != inf else "INF"

for ans in ans_list:
    print(*ans)
