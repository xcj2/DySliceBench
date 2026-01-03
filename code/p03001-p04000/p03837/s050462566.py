class MakeGraph:
    
    # 隣接行列もしくは隣接リストの初期化
    # node_num：ノード数
    # isMat：隣接行列(True) / 隣接リスト(False)
    def __init__(self, node_num:int, isMat:bool) -> None:
        self.n = node_num
        self.isMat = isMat

        # 隣接行列の初期化
        if self.isMat:
            INF = float("inf")
            self.graph = [[INF for _ in range(self.n)] for _ in range(self.n)]
    
        # 隣接リストの初期化
        else:
            self.graph = [[] for _ in range(self.n)]

    # エッジの追加
    # frm, to：起点ノード, 終点ノード
    # dist：frm→toへのコスト
    def add_undr_edge_mat(self, frm:int, to:int, dist:int) -> None:
        self.graph[frm][to] = dist
        self.graph[to][frm] = dist
        
    def add_drct_edge_mat(self, frm:int, to:int, dist:int) -> None:
        self.graph[frm][to] = dist
        
    def add_undr_edge_lst(self, frm:int, to:int, dist:int) -> None:
        self.graph[frm].append((dist, to))
        self.graph[to].append((dist, frm))
        
    def add_drct_edge_lst(self, frm:int, to:int, dist:int) -> None:
        self.graph[frm].append((dist, to))

                
    # 完成したグラフを取り出す
    def get_graph(self) -> list:
        return self.graph
    
N,M = map(int, input().split())
ABC = []
for i in range(M):
    ABC.append(tuple(map(int, input().split())))
    
graphMaker = MakeGraph(N,True)
distMaker = MakeGraph(N,True)
add_edge = graphMaker.add_undr_edge_mat
add_edge2 = distMaker.add_undr_edge_mat
for a,b,c in ABC:
    add_edge(a-1, b-1, c)
    add_edge2(a-1, b-1, c)

graph = graphMaker.get_graph()
dist = distMaker.get_graph()

# WF
for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
            
ans = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != float("inf") and graph[i][j] != dist[i][j]:
            ans += 1

  
print(ans//2)   
