class BST:
  def __init__(self):
    self.root = None
  
  def insert(self, data):
    z = Node(data)
    y = None
    x = self.root

    while x:
      y = x
      if z.data < x.data:
        x = x.left
      else:
        x = x.right
    z.parent = y
    if y == None:
      self.root = z
    elif z.data < y.data:
      y.left = z
    else:
      y.right = z

  def find(self, data):
    x = self.root
    z = Node(data)
    while x and data != x.data:
      if z.data < x.data:
        x = x.left
      else:
        x = x.right
    if x is not None:
      return True
    else:
      return False


  def print(self):
    print('',' '.join(map(str, self.root.inorder())))
    print('',' '.join(map(str, self.root.preorder())))


class Node():
  def __init__(self, data):
    self.data = data
    self.left, self.right = None, None

  def inorder(self):
    in_list = []
    if self.left:
      in_list += self.left.inorder()
    in_list += [self.data]
    if self.right:
      in_list += self.right.inorder()
    return in_list
  
  def preorder(self):
    pre_list = []
    pre_list += [self.data]
    if self.left:
      pre_list += self.left.preorder()
    #pre_list += [self.data]
    if self.right:
      pre_list += self.right.preorder()
    return pre_list

tree = BST()
n = int(input())
for _ in range(n):
  inp = input().split()
  if len(inp) == 2:
    if inp[0] == "insert":
      tree.insert(int(inp[1]))
    else:
      x = tree.find(int(inp[1]))
      if tree.find(int(inp[1])):
        print("yes")
      else:
        print("no")
  else:
    tree.print()

