n = int(input())

class Node:
    def __init__(self):
        self.parent_id = -1
        self.sib = -1
        self.left = -1
        self.right = -1
        self.deg = 0
        self.height = 0
        self.depth = 0
        self.children = []

def cal_depth (node,x):
    node.depth = x

    for children_id in node.children:
        cal_depth(nodes[children_id],x+1)

def cal_height(node):

    h1 = 0
    h2 = 0
    if node.left != -1:
       h1 = cal_height(nodes[node.left]) + 1
    if node.right != -1:
       h2 = cal_height(nodes[node.right]) +1

    node.height = max(h1,h2)

    return max(h1,h2)



nodes = []
for i in range(n):
    nodes.append(Node())

for i in range(n):
    deg = 0
    table = list(map(int,input().split()))
    node_id = table[0]
    nodes[node_id].left = table[1]
    nodes[node_id].right = table[2]
    if table[1] == -1 and table[2] == -1:
        nodes[node_id].deg = 0
    elif table[1] == -1 or table[2] == -1:
        nodes[node_id].deg = 1
        if table[1] != -1:
            nodes[table[1]].parent_id = node_id
            nodes[node_id].children.append(table[1])
        else:
            nodes[table[2]].parent_id = node_id
            nodes[node_id].children.append(table[2])
    else:
        nodes[node_id].deg = 2
        nodes[table[1]].parent_id = node_id
        nodes[table[2]].parent_id = node_id
        nodes[table[1]].sib = table[2]
        nodes[table[2]].sib = table[1]
        nodes[node_id].children.append(table[1])
        nodes[node_id].children.append(table[2])

for node in nodes:
    if node.parent_id == -1:
        cal_depth(node,0)
        cal_height(node)
        break



for i in range(n):

    print("node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, "%(i,nodes[i].parent_id,nodes[i].sib,nodes[i].deg,nodes[i].depth,nodes[i].height),end = "")

    if nodes[i].parent_id == -1:
        print("root")
    else:
        if len(nodes[i].children) == 0: #葉
            print("leaf")
        else: #節
            print("internal node")

