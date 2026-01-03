class Graph():
    def __init__(self):
        """ ノードのつながりを辞書型で表現する """
        self.adjacency_dict = {}
    
    def add_vertex(self, v):
        """ ノードを追加する """
        self.adjacency_dict[v] = []
    def add_edge(self, v1, v2):
        """ ノード同士をつなぐ。"""
        # 無向グラフの場合は双方向。もし有向グラフなら片側のみ。
        self.adjacency_dict[v1].append(v2)
        self.adjacency_dict[v2].append(v1)
    def remove_edge(self, v1, v2):
        """ ノード同士のつながりを削除する。"""
        self.adjacency_dict[v1].remove(v2)
        self.adjacency_dict[v2].remove(v1)
    def remove_vertex(self,v):
        """ ノードを削除する。"""
        while self.adjacency_dict[v] != []:
            adjacent_vertex = self.adjacency_dict[v][-1]
            self.remove_edge(v, adjacent_vertex)
        del self.adjacency_dict[v]
    
    def print_graph(self):
        print(self.adjacency_dict)

    def _init_internal_graph(self, graph_dict):
        self.adjacency_dict = graph_dict
    
    def get_edge(self, v):
        """ 指定されたノードに関するエッジを返す。"""
        return self.adjacency_dict[v]

def dprint(*args):
  if debug:
    if len(args)==1:
      print(args[0])
    else:
      print(args)

debug = False
if debug:
  g = Graph()
  # N,M = [7, 7]
  # g._init_internal_graph({0: [2], 1: [6], 2: [0, 3], 3: [2, 4, 5], 4: [3, 5], 5: [3, 4, 6], 6: [1, 5]})
  
  N,M = [3, 3]
  g._init_internal_graph({0: [1, 2], 1: [0, 2], 2: [0, 1]})
else:
  N, M = map(int, input().split())
  g = Graph()
  dprint(N,M)

  for n in range(N):
    g.add_vertex(n)

  # 0-origin    
  for m in range(M):
      v1,v2 = list(map(int, input().split()))
      g.add_edge(v1-1,v2-1)                     

# g.print_graph()

seen = [False] * N
count = 0

def dfs(node, depth):
    dprint(node,depth)        
    if seen[node]:
        return 0
    if depth == N - 1:
        dprint('count-up',seen)
        return 1

    seen[node] = True
    dprint(seen)
    
    total_paths = 0
    for next_node in g.get_edge(node):
      total_paths += dfs(next_node, depth + 1)

    # seenを未到達にして次へ
    seen[node] = False

    return total_paths

count = dfs(0, 0)
print(count)
