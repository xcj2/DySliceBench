import sys
sys.setrecursionlimit(10**7)

nodedict = {}

class Node:
    def __init__(self, id, left, right):
        self.id = id
        self.parent = -1
        self.depth = -1
        self.sibling = -1
        self.height = -1
        self.left = left
        self.right = right
        self.degree = 0
        if left != -1:
            self.degree += 1
        if right != -1:
            self.degree += 1

    def __repr__(self):
        return str(self.__dict__)

    def get_height(self):
        if self.height != -1:
            pass
        else:
            if self.degree == 0:
                self.height = 0
            else:
                lh, rh = 0, 0
                if self.left != -1:
                    lh = nodedict[self.left].get_height()
                if self.right != -1:
                    rh = nodedict[self.right].get_height()
                self.height = max(lh, rh) + 1

        return self.height

def assign_info(node, current_depth):
    node.depth = current_depth
    if node.left != -1:
        left = nodedict[node.left]
        left.parent = node.id
        left.sibling = node.right
        assign_info(left, current_depth + 1)

    if node.right != -1:
        right = nodedict[node.right]
        right.parent = node.id
        right.sibling = node.left
        assign_info(right, current_depth + 1)

def solve():
    n = int(input())

    # Node作成
    childlist = []
    for i in range(n):
        id, left, right = map(int, input().split())
        nodedict[id] = Node(id, left, right)
        childlist.append(left)
        childlist.append(right)


    # 根を探す
    rootid = -1
    for i in range(n):
        if i not in childlist:
            rootid = i

    # 根から順に情報割り当て
    assign_info(nodedict[rootid], 0)

    # 高さ割り当て
    for i in range(n):
        nodedict[i].get_height()

    # 出力
    for i in range(n):
        node = nodedict[i]
        if node.depth == 0:
            type = "root"
        elif node.height == 0:
            type = "leaf"
        else:
            type = "internal node"

        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(
            node.id, node.parent, node.sibling, node.degree, node.depth, node.height, type))

solve()
