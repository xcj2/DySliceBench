class Node:
  def __init__(self, num):
    self.key = num
    self.p = None
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, z):
    y = None
    x = self.root
    while x != None:
      y = x
      if z.key < x.key:
        x = x.left
      else:
        x = x.right
    z.p = y

    if y is None:
      self.root = z
    elif z.key < y.key:
      y.left = z
    else:
      y.right = z

  def find(self, key):
    node = self.root
    while node:
      if node.key == key: return node
      if key < node.key:
        node = node.left
      else:
        node = node.right
    return None

  def find_minimum(self, node):
    while node.left: node = node.left
    return node

  def delete(self, node):
    if node.left and node.right:
      m = self.find_minimum(node.right)
      node.key = m.key
      self.delete(m)
    elif node.left:
      self.update(node, node.left)
    elif node.right:
      self.update(node, node.right)
    else:
      self.update(node, None)

  def update(self, node, new_node):
    if node.p is None:
      self.root = new_node
      if new_node: new_node.p = None
      return

    if node.key < node.p.key:
      node.p.left = new_node
    else:
      node.p.right = new_node
    if new_node:
      new_node.p = node.p

def print_inorder(node):
  if node is None: return
  print_inorder(node.left)
  print(" {}".format(node.key), end="")
  print_inorder(node.right)

def print_preorder(node):
  if node is None: return
  print(" {}".format(node.key), end="")
  print_preorder(node.left)
  print_preorder(node.right)

T = BinarySearchTree()
for i in range(int(input())):
  params = input().split()
  if params[0] == "insert":
    T.insert(Node(int(params[1])))
  elif params[0] == "find":
    if T.find(int(params[1])):
      print("yes")
    else:
      print("no")
  elif params[0] == "delete":
    node = T.find(int(params[1]))
    if node: T.delete(node)
  elif params[0] == "print":
    print_inorder(T.root)
    print("")
    print_preorder(T.root)
    print("")