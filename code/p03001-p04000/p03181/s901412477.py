def ReRooting(n, e, identify):
  edges = [[] for _ in range(n)]
  indexedges = [[] for _ in range(n)]
  for u, v in e:
    indexedges[v].append(len(edges[u]))
    indexedges[u].append(len(edges[v]))
    edges[u].append(v)
    edges[v].append(u)
  dp = [identify]*n
  subdp = [len(edges[i])*[identify] for i in range(n)]
  parents = [-1]*n
  order = [0]
  for node in order:
    for mode in edges[node]:
      if mode == parents[node]:
        continue
      order.append(mode)
      parents[mode] = node
  def merge1(a, b):
    return a*b%mod
  def addnode1(a, id):
    return a+1
  for node in order[1::][::-1]:
    parent = parents[node]
    ans = identify
    indexparent = -1
    for j in range(len(edges[node])):
      mode = edges[node][j]
      if parent == mode:
        indexparent = j
        continue
      ans = merge1(ans, subdp[node][j])
    subdp[parent][indexedges[node][indexparent]] = addnode1(ans, node)
  def merge2(a,b):
    return a*b%mod
  def addnode2(a, id):
    return a+1
  for node in order:
    b = [identify]*len(edges[node])
    for i in range(len(edges[node])-1,0,-1):
      b[i-1] = merge2(b[i], subdp[node][i])
    bb = identify
    for i in range(len(edges[node])):
      ans = merge2(bb, b[i])
      subdp[edges[node][i]][indexedges[node][i]] = addnode2(ans, node)
      bb = merge2(bb, subdp[node][i])
    dp[node] = addnode2(bb, node)
  return dp
n,mod=map(int,input().split())
edges=[]*n
for _ in range(n-1):
  a,b=map(int,input().split())
  a-=1
  b-=1
  edges.append([a,b])
for i in ReRooting(n,edges,1):print(i-1)