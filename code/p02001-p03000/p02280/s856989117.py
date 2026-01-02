

class Node():
  def __init__(self, id):
    self.id = id
    self.parent = self.right = self.left = None
    self.depth = -1
    self.height = -1
    self.degree = -1
    self.sibiling = -1

class BinaryTree():
  def __init__(self, node_ids, child_info):
    self.root = None
    tmp = sorted(zip(node_ids, child_info), key=lambda x:x[0])
    node_ids = [x[0] for x in tmp]
    child_info = [x[1] for x in tmp]
    self.nodes = [Node(x) for x in node_ids]
    for n, c in zip(self.nodes, child_info):
      self.set_children(n, *c)
    self.set_root()
    self.set_depth(self.root, 0)
    self.set_height()
    self.set_sibilings()
  
  def set_root(self):
    for n in self.nodes:
      if n.parent is None:
        self.root = n
    
  def set_children(self, node, left, right):
    degree = 0
    if left != -1:
      node.left = self.nodes[left]
      node.left.parent = node
      degree += 1
    if right != -1:
      node.right = self.nodes[right]
      node.right.parent = node
      degree += 1
    node.degree = degree 

  def set_depth(self, node, d):
    node.depth = d
    if node.left is not None:
      self.set_depth(node.left, d + 1)
    if node.right is not None:
      self.set_depth(node.right, d + 1)
  
  def set_height(self):
    def get_height(n:Node):
      h1=0
      h2 = 0
      if n.left is not None:
        h1 = get_height(n.left) + 1
      if n.right is not None:
        h2 = get_height(n.right) + 1
      n.height = max(h1,h2)
      return max(h1,h2)
    get_height(self.root)
    
  
  def set_sibilings(self):
    for n in self.nodes:
      if n.parent is None:
        n.sibiling = -1
      else:
        if n.parent.right is not None and n.parent.right != n:
          n.sibiling = n.parent.right.id
        elif n.parent.left is not None and n.parent.left != n: 
          n.sibiling = n.parent.left.id
        else:
          n.sibiling = -1

def print_node(n: Node):
  if n.parent is None:
    ntype = "root"
  elif n.right is None and n.left is None:
    ntype = "leaf"
  else:
    ntype = "internal node"
  template = "node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}"
  parent = n.parent.id if n.parent is not None else -1
  print(template.format(n.id, parent, n.sibiling, n.degree, n.depth, n.height, ntype))


def main():
  n = int(input())
  tmp = [list(map(int, input().split())) for _ in range(n)]
  n = [x[0] for x in tmp]
  c = [x[1:] for x in tmp]
  T = BinaryTree(n,c)
  nodes = T.nodes
#  nodes = sorted(nodes, key=lambda x:x.id)
  for n in nodes:
    print_node(n)

if __name__ == "__main__":
  import sys, io

  main()


