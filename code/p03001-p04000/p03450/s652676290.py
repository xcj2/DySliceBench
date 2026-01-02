from collections import deque

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


class DfsAndBfs:
 
  # グラフは隣接リスト 0-originであることに注意
  # graph[i]はi番目のノードと隣り合うノードの(距離, ノード番号)を格納している
  # 例：0番と3番の距離が7 -> graph[0] = [[(7,3)]] 
  @classmethod
  def dfs(cls, graph:list, node:int) -> list:
    # 未探索のノードは距離を-1とする
    INF = float("inf")
    dist = [-INF]*node  
    
    # 未探索ノードの距離を0とする
    for n in range(node):
        if dist[n] != -INF:
            continue
        else:
            stack = [n]
            dist[n] = 0
            
        # stackが空になるまで探索を繰り返す
        while len(stack):
            cur = stack.pop()
            
            # ノードcurと隣り合う未探索ノードをstackに追加
            for cost, nex_node in graph[cur]:
                if dist[nex_node] != -INF:
                    continue
                else:
                    dist[nex_node] = dist[cur] + cost
                    stack.append(nex_node)

    return dist
 
  
  # グラフは隣接リスト 0-originであることに注意
  # graph[i]はi番目のノードと隣り合うノードの(距離, ノード番号)を格納している
  # 例：0番と3番の距離が7 -> graph[0] = [[(7,3)]]
  @classmethod
  def bfs(cls, graph:list, node:int) -> list:
      # 未探索のノードは距離を-1とする
      INF = float("inf")
      dist = [-INF]*node

      # 未探索ノードの距離を0とする
      for n in range(node):
          if dist[n] != -INF:
              continue
          else:
              que = deque([n])
              dist[n] = 0

          # queが空になるまで探索を繰り返す
          while len(que):
              cur = deque.popleft(que)

              # ノードcurと隣り合う未探索ノードをqueに追加
              for cost, nex_node in graph[cur]:
                  if dist[nex_node] != -INF:
                      continue
                  else:
                      dist[nex_node] = dist[cur] + cost
                      que.append(nex_node)

      return dist
  

N,M = map(int ,input().split())
LRD = []
for i in range(M):
    LRD.append(tuple(map(int ,input().split())))

graphMaker = MakeGraph(N, False)
add_edge = graphMaker.add_drct_edge_lst
for l,r,d in LRD:
    add_edge(l-1,r-1,d)
    add_edge(r-1,l-1,-d)
    
graph = graphMaker.get_graph()

dist = DfsAndBfs.dfs(graph, N)



consistent = True

for l,r,d in LRD:
    if dist[r-1] - dist[l-1] == d:
        continue
    else:
        consistent = False
        break

    
if consistent:
    print("Yes")
else:
    print("No")

