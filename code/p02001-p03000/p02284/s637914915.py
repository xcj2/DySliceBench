class Node:
  def __init__(self, key):
    self.key = key
    self.right = None
    self.left = None

class BST:
  root = None
  def insert(self, key):
    x = self.root
    y = None
    z = Node(key)
    while x != None:
      y = x
      if(z.key < y.key):
        x = x.left
      elif(y.key < z.key):
        x = x.right
    
    if y is None:
      # 初回
      self.root = z
    else:
      if z.key < y.key:
        y.left = z
      elif y.key < z.key:
        y.right = z
        
  def preorder(self, par):
    if par is not None:
      print(" {}".format(par.key), end="")
      self.preorder(par.left)
      self.preorder(par.right)
  
  def inorder(self, par):
    if par is not None:
      self.inorder(par.left)
      print(" {}".format(par.key), end="")
      self.inorder(par.right)
      
  def find(self, key):
    x = self.root
    y = None
    z = Node(key)
    flag = False
    while x != None: 
      y = x
      if(z.key < y.key):
        x = x.left
      elif(y.key < z.key):
        x = x.right
      else:
        flag = True
        break
    return flag
    
  
n = int(input())
bst = BST()
for _ in range(n):
  query = input().split()
  if query[0] == "insert":
    bst.insert(int(query[1]))
  elif query[0] == "find":
    print("yes" if bst.find(int(query[1])) else "no")
  elif query[0] == "print":
    # 中間巡回順, 先行巡回順
    root = bst.root
    bst.inorder(root)
    print()
    bst.preorder(root)
    print()

