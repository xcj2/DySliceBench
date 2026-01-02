from collections import defaultdict

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = -1


preorder, inorder, postorder = [], [], []

def preorder_dfs(root):
  if root is None: return

  preorder.append(root.val)

  preorder_dfs(root.left)
  preorder_dfs(root.right)

def inorder_dfs(root):
  if root is None: return

  inorder_dfs(root.left)

  inorder.append(root.val)

  inorder_dfs(root.right)


def postorder_dfs(root):
  if root is None: return 
  
  postorder_dfs(root.left)
  postorder_dfs(root.right)

  postorder.append(root.val) 


num = int(input())
nodes = defaultdict(int)

for i in range(num):
  val, left, right = list(map(int, input().split()))

  if nodes[val] == 0:
    nodes[val] = TreeNode(val)
  n = nodes[val]
  
  if left != -1:
    # initalize treenode
    if nodes[left] == 0:
      nodes[left] = TreeNode(left)

    # appending to n.left
    n.left = nodes[left]
    n.left.parent = n.val

  if right != -1:
    if nodes[right] == 0:
      nodes[right] = TreeNode(right)

    n.right = nodes[right]
    n.right.parent = n.val

root = [node for node in nodes.values() if node.parent == -1][0]

preorder_dfs(root)
inorder_dfs(root)
postorder_dfs(root)

print("Preorder")
print(" " + " ".join([ str(i) for i in preorder]))
print("Inorder")
print(" " + " ".join([ str(i) for i in inorder]))
print("Postorder")
print(" " + " ".join([ str(i) for i in postorder]))
