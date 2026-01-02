def get_unvisted_child(v, timestamp):
  while len(G[v]) > 0:
    c = G[v].pop(0)
    if not c in timestamp: return c
  return -1

def get_unvisited_node(G, timestamp):
  for v in sorted(G):
    if not v in timestamp: return v
  return -1

def dept_first_search(G):
  t = 1
  timestamp = {}
  stack = []

  v = get_unvisited_node(G, timestamp)
  while v > 0:
    stack.append(v)
    timestamp[v] = [t]
    t += 1

    while len(stack) > 0:
      v = stack[-1]
      c = get_unvisted_child(v, timestamp)
      if c > 0:
        #c = G[v].pop(0)
        stack.append(c)
        timestamp[c] = [t]
      else:
        timestamp[v].append(t)
        stack.pop()
      t += 1

    v = get_unvisited_node(G, timestamp)

  for v in sorted(timestamp):
    print(v, *timestamp[v])

G = {}
for i in range(int(input())):
  x = list(map(int, input().split()))
  G[x[0]] = x[2:]

dept_first_search(G)