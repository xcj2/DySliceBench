class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1

def getDepth(u):
    d = 0
    while Nodes[u].parent != -1:
        u = Nodes[u].parent
        d += 1
    return d

def printChildren(u):
    c = Nodes[u].left
    output_list = []
    while c != -1:
        output_list.append(c)
        c = Nodes[c].right
    return output_list

# ノードの情報を出力する。
def printNodes(u):
    output_str = "node " + str(u) + ": parent = " + str(Nodes[u].parent) + ", depth = " + str(getDepth(u))
    if -1 == Nodes[u].parent:
        output_str = output_str + ", root, "
    elif Nodes[u].left != -1:
        output_str = output_str + ", internal node, "
    else:
        output_str = output_str + ", leaf, "
    # output_str += printChildren(u)
    print(output_str, "[{}]".format(", ".join(map(str, printChildren(u)))), sep="")

Nodes = []
for i in range(100000):
    tmp_obj = Node()
    Nodes.append(tmp_obj)

# 入力
n = int(input())


for tmp_count in range(n):
    input_val = list(map(int, input().split()))
    if 0 != input_val[1]:
        # 最も左の子の情報
        Nodes[input_val[0]].left = input_val[2]
        # 親の情報
        Nodes[input_val[2]].parent = input_val[0]
        
        for i in range(input_val[1] - 1):
            # 右の兄弟の情報
            Nodes[input_val[i+2]].right = input_val[i+3]
            # 親の情報
            Nodes[input_val[i+3]].parent = input_val[0]

for i in range(n):
    printNodes(i)
