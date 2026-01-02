class Node:
    def __init__(self, key, pri):
        self.left = None
        self.right = None
        self.key = key
        self.pri = pri

    def print_pre(self):
        yield self.key
        if self.left:
            for k in self.left.print_pre(): yield k
        if self.right:
            for k in self.right.print_pre(): yield k

    def print_in(self):
        if self.left:
            for k in self.left.print_in(): yield k
        yield self.key
        if self.right:
            for k in self.right.print_in(): yield k

class Tree:
  root = None

  def rightRotate(self, node):
    s = node.left
    node.left = s.right
    s.right = node
    if self.root == node:
      self.root = s
    return s

  def leftRotate(self, node):
    s = node.right
    node.right = s.left
    s.left = node
    if self.root == node:
      self.root = s
    return s

  def insert1(self, node, key, pri):
    if node == None:
      return Node(key, pri)
    elif key == node.key:
      return node

    elif key < node.key:
      node.left = self.insert1(node.left, key, pri)
      if node.pri < node.left.pri:
        node = self.rightRotate(node)
    else:
      node.right = self.insert1(node.right, key, pri)
      if node.pri < node.right.pri:
        node = self.leftRotate(node)
    return node

  def insert(self, key, pri):
    self.insert1(self.root, key, pri)
    if self.root == None:
      self.root = Node(key, pri)

  def delete(self, node, key):
    if node == None:
      return None
    if key < node.key:
      node.left = self.delete(node.left, key)
    elif key > node.key:
      node.right = self.delete(node.right, key)
    else:
      return self.delete1(node, key)
    return node

  def delete1(self, node, key):
    if node.left == None and node.right == None:
      return None
    elif node.left == None:
      node = self.leftRotate(node)
    elif node.right == None:
      node = self.rightRotate(node)
    else:
      if node.left.pri > node.right.pri:
        node = self.rightRotate(node)
      else:
        node = self.leftRotate(node)
    return self.delete(node, key)

  def find(self, key):
        y = None
        x = self.root
        while x:
            y = x
            if key == x.key:
              break
            elif key < x.key:
              x = x.left
            else:
              x = x.right
            
        if key == y.key:
            return y

  def print(self):
        print(' ', end='')
        print(*self.root.print_in())
        print(' ', end='')
        print(*self.root.print_pre())

tree = Tree()
m = int(input())

while m:
  l = input().split()
  if len(l) == 3:
    tree.insert(int(l[1]), int(l[2]))
  elif len(l) == 2 and l[0] == "find":
    y = tree.find(int(l[1]))
    if y:
      print("yes")
    else:
      print("no")
  elif len(l) == 2 and l[0] == "delete":
    tree.delete(tree.root, int(l[1]))
  else:
    tree.print()
  m -= 1
