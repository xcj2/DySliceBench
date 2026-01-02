class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Bst:
  def __init__(self):
    self.root = None

  def insert(self, val):
    node = TreeNode(val)
    if self.root is None: 
      self.root = node
      return

    cur_parent = None
    cur_root = self.root

    while cur_root is not None:
      cur_parent = cur_root
      if val > cur_root.val:
        cur_root = cur_root.right
      else:
        cur_root = cur_root.left

    if val > cur_parent.val:
      cur_parent.right = node
    else:
      cur_parent.left = node

  def find(self, val):
    cur_node = self.root

    while cur_node is not None:
      if cur_node.val == val:
        print("yes")
        return
      elif cur_node.val > val:
        cur_node = cur_node.left
      else:
        cur_node = cur_node.right

    print("no")
    return

  def print(self):
    self.inorder = []
    self.preorder = []
    self.inorder_dfs(self.root)
    self.preorder_dfs(self.root)

    print(" " + " ".join([ str(i) for i in self.inorder ]))
    print(" " + " ".join([ str(i) for i in self.preorder ]))

  def inorder_dfs(self, root):
    if not root: return

    self.inorder_dfs(root.left)
    self.inorder.append(root.val)
    self.inorder_dfs(root.right)

  def preorder_dfs(self, root):
    if not root: return

    self.preorder.append(root.val)
    self.preorder_dfs(root.left)
    self.preorder_dfs(root.right)


n = int(input())
bst = Bst()
for _ in range(n):
  ins = list(map(str, input().split()))
  order = ins[0]
  if order == "insert":
    val = int(ins[1])
    bst.insert(val)
  elif order == "find":
    val = int(ins[1])
    bst.find(val)
  elif order == "print":
    bst.print()




