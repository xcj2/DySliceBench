# coding: utf-8
import queue

class Node:
    def __init__(self, myNum, left, right):
        self.myNum = myNum
        self.left = left
        self.right = right
        self.parent = -1
        self.bs = -1
        self.nodeType = ""
        self.degree = -1
        self.depth = -1
        self.height = -1


n = int(input().rstrip())
preorder = [int(i)-1 for i in input().rstrip().split()]
inorder = [int(i)-1 for i in input().rstrip().split()]
nodes = []

# reconstruct the origin
def createTree(preorder, inorder):
    if not preorder:
        return -1
    if not inorder:
        return -1
    parent = preorder[0]
    pidx = inorder.index(parent)
    leftInorder = inorder[:pidx]
    rightInorder = inorder[pidx+1:]
    leftPreorder = []
    rightPreorder = []
    for item in preorder:
        if item in leftInorder:
            leftPreorder.append(item)
        if item in rightInorder:
            rightPreorder.append(item)
    left = createTree(leftPreorder,leftInorder)
    right = createTree(rightPreorder,rightInorder)
    nodes.append(Node(parent, left, right))
    return parent

createTree(preorder, inorder)
nodes = sorted(nodes, key = lambda x: x.myNum)

# 親ノード、degreeを設定する
for node in nodes:
    dg = 0
    if node.left != -1:
        nodes[node.left].parent = node.myNum
        dg += 1
    if node.right != -1:
        nodes[node.right].parent = node.myNum
        dg += 1
    node.degree = dg
 
# 兄弟ノードを設定する
for node in nodes:
    if node.left != -1 and node.right != -1:
        nodes[node.left].bs = nodes[node.right].myNum
        nodes[node.right].bs = nodes[node.left].myNum
 
# nodeTypeを設定する
for node in nodes:
    if node.parent == -1:
        node.nodeType = "root"
        node.depth = 0
        rootNum = node.myNum
    elif node.left == -1 and node.right == -1:
        node.nodeType = "leaf"
    else:
        node.nodeType = "internal node"
 
# depthを設定する
q = queue.Queue()
q.put(nodes[rootNum])
while not q.empty():
    nd = q.get()
    if nd.left != -1:
        nodes[nd.left].depth = nd.depth + 1
        q.put(nodes[nd.left])
    if nd.right != -1:
        nodes[nd.right].depth = nd.depth + 1
        q.put(nodes[nd.right])
 
# heightを設定する
for node in nodes:
    if node.parent == -1 or node.nodeType == "leaf":
        node.height = 0
        q.put(node)
while not q.empty():
    nd = q.get()
    if nd.parent != -1:
        nodes[nd.parent].height = max(nodes[nd.parent].height, nd.height + 1)
        q.put(nodes[nd.parent])

ans = []

# Preorder
def dfsPreorder(x):
    if nodes[x].height == 0:
        ans.append(x)
        return
    
    ans.append(nodes[x].myNum)
    if nodes[x].left != -1:
        dfsPreorder(nodes[x].left)
    if nodes[x].right != -1:
        dfsPreorder(nodes[x].right)

# Inorder
def dfsInorder(x):
    if nodes[x].height == 0:
        ans.append(x)
        return
    
    if nodes[x].left != -1:
        dfsInorder(nodes[x].left)
    ans.append(nodes[x].myNum)
    if nodes[x].right != -1:
        dfsInorder(nodes[x].right)
    
# Postorder
def dfsPostorder(x):
    if nodes[x].height == 0:
        ans.append(x+1)
        return
    
    if nodes[x].left != -1:
        dfsPostorder(nodes[x].left)
    if nodes[x].right != -1:
        dfsPostorder(nodes[x].right)
    ans.append(nodes[x].myNum+1)

dfsPostorder(rootNum)
print(" ".join(str(i) for i in ans))
