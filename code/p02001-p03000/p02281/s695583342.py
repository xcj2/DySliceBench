class Node:
  def __init__(self, id):
    self.id = id
    self.parent = None
    self.left = None
    self.right = None

def preParse(node):
  if node == None:
    return
  print(" {}".format(node.id), end="")
  preParse(node.left)
  preParse(node.right)

def inParse(node):
  if node == None:
    return
  inParse(node.left)
  print(" {}".format(node.id), end="")
  inParse(node.right)

def postParse(node):
  if node == None:
    return
  postParse(node.left)
  postParse(node.right)
  print(" {}".format(node.id), end="")

num = int(input())
nodes = [None] * num
for i in range(num):
  id, left, right = map(int, input().split())
  node = nodes[id] if nodes[id] else Node(id)
  nodes[id] = node

  if left != -1:
    if nodes[left]:
      nodes[left].parent = node
      node.left = nodes[left]
    else:
      l = Node(left)
      l.parent = node
      node.left = l
      nodes[left] = l

  if right != -1:
    if nodes[right]:
      nodes[right].parent = node
      node.right = nodes[right]
    else:
      r = Node(right)
      r.parent = node
      node.right = r
      nodes[right] = r

def getParent(node):
  if node.parent == None:
    return node
  return getParent(node.parent)

print("Preorder")
preParse(getParent(nodes[0]))
print()
print("Inorder")
inParse(getParent(nodes[0]))
print()
print("Postorder")
postParse(getParent(nodes[0]))
print()
