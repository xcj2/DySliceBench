import sys
sys.setrecursionlimit(1000000)

class Tree():
    def __init__(self, parent, child, sibling):
        self.parent = parent
        self.child = child  # 最も左の子left child
        self.sibling = sibling  # すぐ右の兄弟right sibling
        self.depth = -1

    def gettreetype(self):
        if self.parent == -1:
            return "root"
        if self.child == -1:
            return "leaf"
        return "internal node"


def setdepth(id, depth, trees):
    trees[id].depth = depth
    child = trees[id].child
    if child >= 0:
        setdepth(child, depth + 1, trees)
    sibling = trees[id].sibling
    if sibling >= 0:
        setdepth(sibling, depth, trees)


def getroot(trees, n):
    for i in range(n):
        if trees[i].parent == -1:
            return i


def getsiblings(tree, trees):
    siblings = []
    sibling = tree.sibling
    while sibling > -1:
        siblings.append(sibling)
        sibling = trees[sibling].sibling
    return siblings


def getchildren(tree, trees):
    children = []
    child = tree.child
    if child > -1:
        children.append(child)
        sibling = trees[child].sibling
        while sibling > -1:
            children.append(sibling)
            sibling = trees[sibling].sibling
    return children


def settree(node_info, trees):
    id = node_info[0]
    dim = node_info[1]
    children = node_info[2:]
    trees[id].child = children[0]
    for i in range(dim):
        trees[children[i]].parent = id
        trees[children[i]].sibling = children[i + 1]


def printtrees(trees, n):
    for i in range(n):
        tree = trees[i]
        parent = tree.parent
        depth = tree.depth
        tree_type = tree.gettreetype()
        children = getchildren(tree, trees)
        print("node {}: parent = {}, depth = {}, {}, [{}]".format(
            i, parent, depth, tree_type, ", ".join(map(str, children))))


def main():
    n = int(input())
    trees = [Tree(-1, -1, -1) for _ in range(n)]
    for _ in range(n):
        node_info = input().split(" ")
        node_info = list(map(int, node_info)) + [-1]
        settree(node_info, trees)
    root = getroot(trees, n)
    setdepth(root, 0, trees)
    printtrees(trees, n)


if __name__ == "__main__":
    main()

