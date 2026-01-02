class Node():
  def __init__(self):
    self.parent = -1
    self.left = -1
    self.right = -1

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

def get_hight(H, u):
  lh, rh = 0, 0
  if result[u].left != -1:
    lh = get_hight(H, result[u].left)+1
  if result[u].right != -1:
    rh = get_hight(H, result[u].right)+1

  H[u] = max(lh, rh)
  return H[u]

n = int(input())
node  = [list(map(int, input().split())) for _ in range(n)] 
result = [Node() for _ in range(n)]
D = [0 for _ in range(n)]
H = [0 for _ in range(n)]


def initiate(li):
  for l in li:
    n = l[0]
    left = l[1]
    right = l[2]
    if left != -1:
      result[left].parent = n
      result[n].left = left
    if right != -1:
      result[right].parent = n
      result[n].right = right


initiate(node)

for u in range(n):
  get_depth_1(u, 0)
  
for u in range(n):
    get_hight(H, u)

final = []

for i in range(n):
  node = i 
  parent = result[node].parent 
  depth = D[i]
  height = H[i]
  degree = 0
  if result[node].left == -1 and result[node].right == -1:
    typ = "leaf"
    degree = 0
  elif result[node].left >= 0 and result[node].right >= 0:
    typ = "internal node"
    degree = 2
  else:
    degree = 1
    typ = "internal node"

  if parent == -1:
    typ = "root"
  if result[parent].left == node:
    sibling = result[parent].right
  else:
    sibling = result[parent].left
  print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(node, parent, sibling, degree, depth, height, typ))

