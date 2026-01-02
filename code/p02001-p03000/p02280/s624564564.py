from collections import defaultdict

class TreeNode():

  def __init__(self, val):
    self.val = val
    self.parent = -1
    self.sibling = -1
    self.left = None
    self.right = None
    self.depth = -1
    self.height = -1

  def node_type(self):
    if self.depth == 0:
      return "root"
    elif self.left or self.right:
      return "internal node"
    else:
      return "leaf"

  def get_degree(self):
    deg = 0
    if self.left: deg += 1
    if self.right: deg += 1

    return deg

  def __str__(self):
    # degree = num of children
    return "node {0}: parent = {1}, sibling = {2}, degree = {3}, depth = {4}, height = {5}, {6}".format(
      str(self.val), str(self.parent), str(self.sibling), str(self.get_degree()), str(self.depth), str(self.height), str(self.node_type()))

def calc_depth(root, level):
  if root is None: return
  root.depth = level

  calc_depth(root.left, level+1)
  calc_depth(root.right, level+1)

def calc_height(root):
  if root is None: return 0

  leftHeight = calc_height(root.left)
  rightHeight = calc_height(root.right)

  return 1 + max(leftHeight, rightHeight)

num = int(input())
nodes = defaultdict(int)

for i in range(num):
  ins = list(map(int, input().split()))
  val = ins[0]

  if nodes[val] == 0:
    nodes[val] = TreeNode(val)
  n = nodes[val]

  left_val, right_val = ins[1], ins[2]
  
  if left_val != -1:
    # initalize treenode
    if nodes[left_val] == 0:
      nodes[left_val] = TreeNode(left_val)

    # appending to n.left
    n.left = nodes[left_val]
    n.left.parent = n.val
    # get sibling
    if right_val != -1:
      n.left.sibling = right_val

  if right_val != -1:
    if nodes[right_val] == 0:
      nodes[right_val] = TreeNode(right_val)

    n.right = nodes[right_val]
    n.right.parent = n.val
    if left_val != -1:
      n.right.sibling = left_val

root = [node for node in nodes.values() if node.parent == -1][0]
calc_depth(root, 0)
for i in range(num):
  n  = nodes[i]
  n.height = calc_height(n) - 1

sort_nodes = sorted(nodes.items(), key=lambda x:x[0] )
for _, node in sort_nodes:
  print(node)
