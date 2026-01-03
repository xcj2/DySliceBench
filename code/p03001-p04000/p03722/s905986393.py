class Dijkstra():
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK

    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """
    class Edge():
        """ 重み付き有向辺 """
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        """ 重み付き有向辺
        無向辺を表現したいときは、_fromと_toを逆にした有向辺を加えればよい

        Args:
            V(int): 頂点の数
        """
        self.G = [[] for i in range(V)]  # 隣接リストG[u][i] := 頂点uのi個目の隣接辺
        self._E = 0  # 辺の数
        self._V = V  # 頂点の数

    @property
    def E(self):
        """ 辺数
        無向グラフのときは、辺数は有向グラフの倍になる
        """
        return self._E

    @property
    def V(self):
        """ 頂点数 """
        return self._V

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1

    def shortest_path(self, s):
        """ 始点sから頂点iまでの最短路を格納したリストを返す
        Args:
            s(int): 始点s
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短コストを格納したリスト。
                     到達不可の場合、値はfloat("inf")
        """
        import heapq
        que = []  # プライオリティキュー（ヒープ木）
        d = [10**15] * self.V
        d[s] = 0
        heapq.heappush(que, (0, s))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost  # dの更新
                    heapq.heappush(que, (d[e.to], e.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush
        return d

def BellmanFord(edges,num_v,source):
  #グラフの初期化
  inf=float("inf")
  dist=[inf for i in range(num_v)]
  dist[source-1]=0

  #辺の緩和
  for i in range(num_v):
    for edge in edges:
      if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
        dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
        if i==num_v-1: return -1

  return dist

N,M=map(int,input().split())
edges=[]
test=Dijkstra(N)
for i in range(0,M):
    a,b,c=map(int,input().split())
    edges.append([a,b,-c])
    test.add(b-1,a-1,1)

use=set([N-1])
for i in range(0,N-1):
    if test.shortest_path(N-1)[i]!=10**15:
        use.add(i)

useedges=[]
for i in range(0,M):
    a,b,c=edges[i]
    if a-1 in use and b-1 in use:
        useedges.append(edges[i])

ans=BellmanFord(useedges,N,1)
if ans==-1:
    print('inf')
else:
    print(-ans[N-1])
