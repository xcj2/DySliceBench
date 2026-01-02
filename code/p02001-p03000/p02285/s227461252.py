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
    return x
    """if x is not None:
      return True
    else:
      return False"""

  def getMinimum(self, z):
    while z.left:
      z = z.left
    return z

  def getSuccessor(self, z):
    if z.right:
      return self.getMinimum(z.right)
    
    y = z.parent
    while y and z == y.right:
      z = y
      y = y.parent
    return y
      
  def delete(self, data):
    z = self.find(data)
    if z is None:
      return 

    #z = Node(data)
    if (z.left is None) or (z.right is None):
      y = z
    else:
      y = self.getSuccessor(z)

    if y.left is not None:
      x = y.left
    else:
      x = y.right
    
    if x is not None:
      x.parent = y.parent

    if y.parent is None:
      self.root = x
    elif y == y.parent.left:
      y.parent.left = x
    else:
      y.parent.right = x

    if y != z:
      z.data = y.data

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
    elif inp[0] == "find":
      x = tree.find(int(inp[1]))
      if x is not None:
        print("yes")
      else:
        print("no")
    else:
      tree.delete(int(inp[1]))
  else:
    tree.print()

