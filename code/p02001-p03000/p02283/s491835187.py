class Node():
   def __init__(self, key):
     self.parent = None
     self.right = None
     self.left = None
     self.key = key

class BST():
  def __init__(self):
    self.T = list()
    self.root = None
    self.res = []

  def insert(self,node:Node):
    y = None
    x = self.root
    while x is not None:
      y = x
      if node.key < x.key:
        x = x.left
      else:
        x = x.right
    node.parent = y
    if y is None:
      self.root = node
    elif node.key < y.key:
      y.left = node
    else:
      y.right = node

  def preorder(self,node:Node):
    if node is None:
      return
    #self.res.append(node.key)
    print(" " + str(node.key), end="")
    self.preorder(node.left)
    self.preorder(node.right)

  def inorder(self, node:Node):
    if node is None:
      return
    self.inorder(node.left)
    print(" " + str(node.key), end="")
    self.res.append(node.key)
    self.inorder(node.right)




def main():
  n = int(input())
  T = BST()
  for _ in range(n):
    cmd = input().split()
    if cmd[0] == "insert":
      key = int(cmd[1])
      T.insert(Node(key))
    else:
#      T.res = list()
      T.inorder(T.root)
      print()
#      print(" ".join(map(str,T.res)))
#      T.res = list()
      T.preorder(T.root)
      print()
#      print(" ".join(map(str,T.res)))

if __name__ == "__main__":
  import sys, io

  main()


