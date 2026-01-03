from heapq import heappush, heappop

def dijkstra(graph:list, node:int, start:int) -> list:
    # 未探索のノードは距離INF
    INF = float("inf")
    dist = [INF]*node
    
    # 始点ノードの距離を0とし、dfsのためのpriority queを作成
    dist[start] = 0
    heap = [(0,start)]
    
    # 未探索のノードをpriority queueに入れる
    while heap:
        cost, cur_node = heappop(heap)
        
        for nex_cost, nex_node in graph[cur_node]:
            dist_cand = dist[cur_node] + nex_cost
            if dist_cand < dist[nex_node]:
                dist[nex_node] = dist_cand
                heappush(heap, (dist[nex_node], nex_node))
    
    return dist

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

# 入力    
N,M = map(int, input().split())
ABC = []
for i in range(M):
    ABC.append(tuple(map(int, input().split())))
    
#file = open("sampleABC051D.txt", "r")
#
#N,M = map(int, file.readline().split())
#ABC = []
#for i in range(M):
#    ABC.append(tuple(map(int, file.readline().split())))
    
graphMaker = MakeGraph(N,False)
add_edge = graphMaker.add_undr_edge_lst

for a,b,c in ABC:
    add_edge(a-1, b-1, c)

graph = graphMaker.get_graph()

dist = []
for i in range(N):
    dist_temp = dijkstra(graph, N, i)
    dist.append(dist_temp)
    
ans = 0
for i in range(N):
    for cost, node in graph[i]:
        if dist[i][node] != cost:
            ans += 1
            
            
print(ans//2)

