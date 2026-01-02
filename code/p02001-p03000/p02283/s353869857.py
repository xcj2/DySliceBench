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
  if params[0] == "print":
    print_inorder(T.root)
    print("")
    print_preorder(T.root)
    print("")