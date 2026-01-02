import sys, os
import collections

MOD = 10 ** 9 + 7

class Edge:
  def __init__(self, to, edge_id):
    super().__init__()
    self.to = to
    self.edge_id = edge_id

class DFSState:
  def __init__(self, vertex, parent_color = -1, parent = -1):
    super().__init__()
    self.vertex = vertex
    self.parent_color = parent_color
    self.parent = parent

def solve(input_stream):
  N = read_int(input_stream)
  graph = [[] for i in range(N)]
  answer = [0 for i in range(N - 1)]
  K = 0
  for index in range(N-1):
    i,j = read_ints(input_stream)
    i-=1
    j-=1
    graph[i].append(Edge(j, index))
    graph[j].append(Edge(i, index))
  dfs = [DFSState(0)]
  while len(dfs) > 0 :
    color = 1
    state = dfs.pop(0)
    for index, value in enumerate(graph[state.vertex]):
      to = value.to
      edge_id = value.edge_id
      if to == state.parent:
        continue
      if color == state.parent_color:
        color += 1
      answer[edge_id] = str(color)
      dfs.append(DFSState(to, color, state.vertex))
      color += 1
  for value in graph:
    K = max(K, len(value))
  ans = [str(K)]
  ans.extend(answer)
  return ans

    


def read_ints(input_stream):
  return [i for i in map(int, input_stream.readline().strip().split())]

def read_int(input_stream):
  return int(input_stream.readline().strip())


if __name__ == "__main__":
    outputs = solve(sys.stdin)
    for line in outputs:
      print(line)