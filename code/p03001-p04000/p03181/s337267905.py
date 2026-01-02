def ReRooting(nodeCount, edges, identity, merge, addNode):
  adjacents = [[] for _ in range(nodeCount)]
  indexForAdjacents = [[] for _ in range(nodeCount)]
  for u,v in edges:
    indexForAdjacents[v].append(len(adjacents[u]))
    indexForAdjacents[u].append(len(adjacents[v]))
    adjacents[u].append(v)
    adjacents[v].append(u)
  childSubtreeRes = [[identity]*len(adjacents[i]) for i in range(nodeCount)]
  nodeRes = [identity]*nodeCount
  parents = [-1]*nodeCount
  order = [0]*nodeCount
  index = 0
  stack = [0]
  for node in stack:
    order[index] = node
    index += 1
    for adjacent in adjacents[node]:
      if adjacent == parents[node]:
        continue
      stack.append(adjacent)
      parents[adjacent] = node
  for node in order[::-1]:
    parent = parents[node]
    result = identity
    parentIndex = -1
    for j in range(len(adjacents[node])):
      if adjacents[node][j] == parent:
        parentIndex = j
        continue
      result = merge(result, childSubtreeRes[node][j])
    if parentIndex >= 0:
      childSubtreeRes[parent][indexForAdjacents[node][parentIndex]] = addNode(result, node)
  for node in order:
    accumsFromTail = [identity]*len(adjacents[node])
    for j in range(len(accumsFromTail)-1, 0, -1):
      accumsFromTail[j-1] = merge(childSubtreeRes[node][j], accumsFromTail[j])
    accum = identity
    for j in range(len(accumsFromTail)):
      result = addNode(merge(accum, accumsFromTail[j]), node)
      childSubtreeRes[adjacents[node][j]][indexForAdjacents[node][j]] = result
      accum = merge(accum, childSubtreeRes[node][j])
    nodeRes[node] = addNode(accum, node)
  return nodeRes

n, mod = map(int, input().split())
edge = []
for _ in range(n-1):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  edge.append((x, y))
def merge(a, b):
  return a*b % mod
def addNode(a, id):
  return a+1
for i in ReRooting(n, edge, 1, merge, addNode):
  print(i-1)
