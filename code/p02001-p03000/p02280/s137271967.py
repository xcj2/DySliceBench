class Node2:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1
    
def getSibling(u):
    if Nodes[u].parent == -1:
        return -1
    p = Nodes[u].parent
    if Nodes[p].left == u:
        return Nodes[p].right
    else:
        return Nodes[p].left

def getDepth(u):
    depth = 0
    while Nodes[u].parent != -1:
        depth += 1
        u = Nodes[u].parent
        
    return depth

def getDegree(u):
    if Nodes[i].left != -1 and Nodes[i].right != -1:
        return 2
    elif Nodes[i].left == -1 and Nodes[i].right == -1:
        return 0
    else:
        return 1

def getHeight(u):
    a = 0
    b = 0
    if Nodes[u].left != -1:
        a = getHeight(Nodes[u].left) + 1
    if Nodes[u].right != -1:
        b = getHeight(Nodes[u].right) + 1
    return max(a, b)

def getType(u):
    if Nodes[u].parent == -1:
        return "root"
    elif Nodes[u].right != -1 or Nodes[u].left != -1:
        return "internal node"
    else:
        return "leaf"
    
def printNode(u):
    print_str = "node " + str(u) + ": parent = " + str(Nodes[u].parent) + ", "
    print_str = print_str + "sibling = " + str(getSibling(u)) + ", "
    print_str = print_str + "degree = " + str(getDegree(u)) + ", "
    print_str = print_str + "depth = " + str(getDepth(u)) + ", "
    print_str = print_str + "height = " + str(getHeight(u)) + ", " + getType(u)
    print(print_str)
    
        

    
# 入力
n = int(input())

Nodes = []
for i in range(n):
    tmp_obj = Node2()
    Nodes.append(tmp_obj)

# 登録作業
for i in range(n):
    num, left, right = map(int, input().split())
    Nodes[num].left = left
    Nodes[num].right = right
    if left != -1:
        Nodes[left].parent = num
    if right != -1:
        Nodes[right].parent = num
    
# 出力
for i in range(n):
    printNode(i)
