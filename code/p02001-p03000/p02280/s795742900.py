class Node():
    def __init__(self):
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = -1
        self.height = -1
        self.type = ""
        self.left = -1
        self.right = -1


def dfs(id, depth=0):
    Nodes[id].depth, Nodes[id].height = depth, 0
    if Nodes[id].left != -1:
        Nodes[id].height = max(
            Nodes[id].height, dfs(Nodes[id].left, depth+1) + 1)
    if Nodes[id].right != -1:
        Nodes[id].height = max(Nodes[id].height, dfs(
            Nodes[id].right, depth+1) + 1)
    return Nodes[id].height


def main():
    n = int(input())
    global Nodes
    Nodes = [Node() for i in range(n)]

    for i in range(n):
        id, *children = map(int, input().split())
        left = children[0]
        right = children[1]
        if left != -1 and right != -1:
            Nodes[id].type = "internal node"
            Nodes[id].degree = 2
            Nodes[id].left = left
            Nodes[id].right = right
            Nodes[left].sibling = right
            Nodes[right].sibling = left
        elif left != -1 or right != -1:
            Nodes[id].type = "internal node"
            Nodes[id].degree = 1
            if left != -1:
                Nodes[id].left = left
            else:
                Nodes[id].left = right
        else:
            Nodes[id].type = "leaf"
            Nodes[id].degree = 0
        for child in children:
            if child != -1:
                Nodes[child].parent = id

    rootid = ""
    for i, node in enumerate(Nodes):
        if node.parent == -1:
            rootid = i
    Nodes[rootid].type = "root"
    dfs(rootid)

    for i, node in enumerate(Nodes):
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(
            i, node.parent, node.sibling, node.degree, node.depth, node.height, node.type))


if __name__ == '__main__':
    main()
