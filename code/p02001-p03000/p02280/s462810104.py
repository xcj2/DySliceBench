
class Node():
    "node of the tree structure"
    def __init__(self, parent = -1, left = -1, right = -1):
        self.parent = parent
        self.left = left
        self.right = right

def setHeight(u):
    h1 = 0
    h2 = 0
    if node_list[u].right != -1:
        h1 = setHeight(node_list[u].right) + 1
    if node_list[u].left != -1:
        h2 = setHeight(node_list[u].left) + 1
    return max(h1,h2)

def getSibling(u):
    if node_list[u].parent == -1:
        return -1
    if node_list[node_list[u].parent].left != -1 and node_list[node_list[u].parent].left != u:
        return node_list[node_list[u].parent].left
    if node_list[node_list[u].parent].right != -1 and node_list[node_list[u].parent].right != u:
        return node_list[node_list[u].parent].right
    return -1

def getDegree(u):
    count = 0
    if node_list[u].left != -1:
        count += 1
    if node_list[u].right != -1:
        count += 1
    return count

def getDepth(u):
    count = 0
    while node_list[u].parent != -1:
        count += 1
        u = node_list[u].parent
    return count

def getType(u):
    if node_list[u].parent == -1:
        return "root"
    if node_list[u].left == -1 and node_list[u].right == -1:
        return "leaf"
    return "internal node"

n = int(input())
node_list = []
for i in range(n):
    node = Node()
    node_list.append(node)

for i in range(n):
    a,b,c = map(int, input().split())
    node_list[a].left = b
    node_list[a].right = c
    if b != -1:
        node_list[b].parent = a
    if c != -1:
        node_list[c].parent = a
height_list = [-1]*n

for i in range(n):
    print("node", str(i)+":", "parent =", str(node_list[i].parent) + ",", "sibling =", str(getSibling(i)) + ",", "degree =", str(getDegree(i)) + ",", "depth =", str(getDepth(i)) + ",", "height =", str(setHeight(i)) + ",", getType(i))

