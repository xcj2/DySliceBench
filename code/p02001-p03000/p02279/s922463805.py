def getDepth(u):
    d = 0
    while node_list[u].parent != -1:
        u = node_list[u].parent
        d += 1
    return d
def getChildren(u):
    c = node_list[u].left
    child_list = []
    while c != -1:
        child_list.append(c)
        c = node_list[c].right
    return child_list

def getType(u):
    if node_list[u].parent == -1:
        return "root"
    if node_list[u].left == -1:
        return "leaf"
    return "internal node"
max_value = 10 ** 10
nil = -1

class Node():
    " node of the tree structure"
    def __init__(self, name = -1, parent = -1, left = -1, right = -1):
        self.name = name
        self.parent = parent
        self.left = left
        self.right = right
node_list = []
n = int(input())
for i in range(n):
    node = Node()
    node_list.append(node)

for i in range(n):
    a,b,*args = map(int, input().split())
    for j in range(b):
        if j == 0:
            node_list[a].left = args[j]
        else:
            node_list[l].right = args[j]
        l = args[j]
        node_list[args[j]].parent = a


#for i in range(n):

for i in range(n):
    print("node", str(i) + ":" , "parent =", str(node_list[i].parent) + ",", "depth =", str(getDepth(i)) + ",", getType(i) + ",", getChildren(i))

