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
        return cur_node
      elif cur_node.val > val:
        cur_node = cur_node.left
      else:
        cur_node = cur_node.right

    return False

  def minValueNode(self, node): 
    current = node 
  
    # loop down to find the leftmost leaf 
    while(current.left is not None): 
        current = current.left  
  
    return current

  def delete(self, root, val):
    if root is None: 
      return root
    elif val < root.val:
      root.left = self.delete(root.left, val)
    elif val > root.val:
      root.right = self.delete(root.right, val)
    else:
      # Node with only one child or no child 
      if root.left is None: 
        temp = root.right  
        root = None 
        return temp  

      elif root.right is None: 
          temp = root.left  
          root = None
          return temp 

      # Node with two children: Get the inorder successor 
      # (smallest in the right subtree) 
      temp = self.minValueNode(root.right) 

      # Copy the inorder successor's content to this node 
      root.val = temp.val 

      # Delete the inorder successor 
      root.right = self.delete(root.right, temp.val) 

    return root  

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
    if not bst.find(val):
      print("no")
    else:
      print("yes")
  elif order == "delete":
    val = int(ins[1])
    bst.delete(bst.root, val)
  elif order == "print":
    bst.print()



