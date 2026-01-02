import sys
sys.setrecursionlimit(10**7)

nodedict = {}

class Node:
    def __init__(self, id, jisu, children):
        self.id = id
        self.jisu = jisu
        self.children = children
        self.parent = -1
        self.depth = -1

    def __repr__(self):
        return "id:{}, jisu:{}, parent:{}, depth:{}, children:{}".format(self.id, self.jisu, self.parent, self.depth, self.children)

def assign_depth(node, current_depth):
    node.depth = current_depth
    for childid in node.children:
        assign_depth(nodedict[childid], current_depth+1)

def solve():
    n = int(input())

    # Node作成
    for i in range(n):
        input_list = list(map(int, input().split()))
        id = input_list[0]
        jisu = input_list[1]
        children = input_list[2:]
        nodedict[id] = Node(id, jisu, children)

    # 親番号の割り当て
    for i in range(n):
        node = nodedict[i]
        for childid in node.children:
            child = nodedict[childid]
            child.parent = node.id

    #print(nodedict)
    # 根探し
    neid = None
    for i in range(n):
        node = nodedict[i]
        if node.parent == -1:
            neid = node.id
            break

    # 深さを割り当てる
    assign_depth(nodedict[neid], 0)

    # 出力
    for i in range(n):
        node = nodedict[i]
        if node.depth == 0:
            type = "root"
        elif len(node.children) == 0:
            type = "leaf"
        else:
            type = "internal node"

        print("node {}: parent = {}, depth = {}, {}, {}".format(node.id, node.parent, node.depth, type, node.children))

solve()
