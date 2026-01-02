import re

class Node:
  key = None
  left = None
  right = None
  def __init__(self, k):
    self.key = k

class BST:
  root = None
  def insert(self, k):
    x = self.root
    y = None
    z = Node(k)
    while x is not None:
      y = x
      if z.key < y.key:
        x = x.left
      elif y.key < z.key:
        x = x.right
    
    if y is None:
      # 初回値
      self.root = z
    else:
      if z.key < y.key:
        y.left = z
      elif y.key < z.key:
        y.right = z
  """      
  def inorder(self, r):
    # 中間巡回順で出力
    if r != None:
      self.inorder(r.left)
      print(" {}".format(r.key), end="")
      self.inorder(r.right)
  """    

  def preorder(self, r, lis):
    # 先行巡回順で出力
    if r != None:
      lis.append(r.key)
      self.preorder(r.left, lis)
      self.preorder(r.right, lis)

    
n = int(input())
bst = BST()
for _ in range(n):
  # query = [int(x) if re.match('[+|-]?\d', x) else x for x in input().split()]
  query = input().split()
  if query[0] == 'insert':
    bst.insert(int(query[1]))
  elif query[0] == 'print':
    root = bst.root
    lis = []
    bst.preorder(root, lis)
    print(" " + " ".join(list(map(str, sorted(lis)))))
    print(" " + " ".join(list(map(str, lis))))
