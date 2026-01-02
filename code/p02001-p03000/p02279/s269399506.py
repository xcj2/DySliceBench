class Node():
  def __init__(self):
    self.parent = -1
    self.left = None
    self.right = None

def get_depth(u, p):
  D[u] = p
  if result[u].right is not None:
    get_depth(result[u].right, p)
  if result[u].left is not None:
    get_depth(result[u].left, p+1)

def get_depth_1(u, p):
  i = u
  d = 0
  while result[u].parent != -1:
    u = result[u].parent
    d += 1
  D[i] = d

n = int(input())
node  = [list(map(int, input().split())) for _ in range(n)] 
result = [Node() for _ in range(n)]
D = [0 for _ in range(n)]

def initiate(li):
  for l in li:
    n = l[0]
    child_num = l[1]
    child = []
    i = 1
    if child_num != 0:
      child = l[2:]
    for c in child:
      if i == 1:
        result[n].left = c 
        i += 1
      else:
        result[idx].right = c 
      idx = c
      result[c].parent = n

initiate(node)
u = 0
for i in range(n):
  if result[i].parent == -1:
    u = i
for u in range(n):
  get_depth_1(u, 0)
final = []
for i in range(n):
  n = i 
  p = result[i].parent
  d = D[i]
  c = [result[i].left]
  j = result[i].left
  if j is not None:
    while result[j].right is not None:
      c.append(result[j].right)
      j = result[j].right
  final.append([n, p, d, c])
  
for i in range(n+1):
  n, p, d, c = final[i]
  typ = ""
  if p == -1:
    typ = "root"
    if c == [None]:
      c = []
  else:
    if c == [None]:
      typ = "leaf"
      c = []
    else:
      typ = "internal node"
  print("node {}: parent = {}, depth = {}, {}, {}".format(n, p, d, typ, c))
