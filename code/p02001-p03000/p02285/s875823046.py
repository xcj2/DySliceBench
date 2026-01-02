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
      # yがターゲットになっているので
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
    while x is not None: 
      y = x
      if(z.key < y.key):
        x = x.left
      elif(y.key < z.key):
        x = x.right
      else:
        flag = True
        break
    return flag
  
  def delete(self, key):
    if self.find(key):
      x = self.root
      y = None

      while x is not None: 
        y = x
        if(key < y.key):
          x = x.left
        elif(y.key < key):
          x = x.right
        else:
          # rootが対象のノードの場合
          break
        if(x.key == key):
          break

      # yが親、子のxがdeleteの対象
      x_children  = [c for c in [x.left, x.right] if c is not None]
      if len(x_children) == 0:
        # 親から子の情報を削除
        for c in [y.left, y.right]:
          if c is not None and c.key == key:
            # yの左右どっちにcがあるのか同定してx_children[0]をぶちこむ
            which_side = [i for i, x in enumerate([y.left, y.right]) if x is not None and x.key == c.key][0]
            if which_side == 0:
              # 左側
              y.left = None
            else:
              # 右側
              y.right = None
      elif len(x_children) == 1:
        # 子の子を親の子にする（字面が妙な雰囲気）
        for c in [y.left, y.right]:
          if c is not None and c.key == key:
            # yの左右どっちにcがあるのか同定してx_children[0]をぶちこむ
            which_side = [i for i, x in enumerate([y.left, y.right]) if x is not None and x.key == c.key][0]
            if which_side == 0:
              # 左側
              y.left = x_children[0]
            else:
              # 右側
              y.right = x_children[0]
      else:
        # 削除予定の子から左側のうち最大のものをとってきて、削除予定のやつを削除したのちそこに入れる
        # とやったらなぜか右側の最小値で出すのが想定される解らしい どっちでもあってんだろが
        min_child = x.right
        # 一つ上の親を保持
        par = x
        while True:
          if min_child.left is None:
            break
          par = min_child
          min_child = min_child.left

        if(par.key == key):
          # 初っ端で終了した（下る世代の数が1）
          pass
        else:
          # 下る世代の数が1より多い
          par.left = None
          min_child.right = x.right
          
        # 大本の削除対象のxの親であるyの左右どちらがxであるか同定し更新
        x_side = [i for i, s in enumerate([y.left, y.right]) if s is not None and s.key == x.key][0]
        # それを直接min_childとする
        if x_side == 0:
          # 左
          y.left = min_child
        else:
          # 右
          y.right = min_child
        # 更新
        min_child.left = x.left
      
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
  elif query[0] == "delete":
    bst.delete(int(query[1]))

