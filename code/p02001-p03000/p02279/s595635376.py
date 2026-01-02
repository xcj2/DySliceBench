import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

tree = []
root_index = []
depths = []


def main():
    n = int(input())

    # 初期化
    for i in range(n):
        tree.append(Node(i, None, None))
        root_index.append(i)
        depths.append(0)

    for i in range(n):
        node_number, _, *c_list = list(map(int, input().split()))
        tree[node_number].child = c_list

        for c in c_list:
            tree[c].parent = tree[node_number]
            root_index.remove(c)

    root = tree[root_index[0]]
    root.parent = Node(-1, None, None)

    setDepth(root, 0)
    showTree(root)


def setDepth(node, d):
    depths[node.number] = d
    for c in node.child:
        setDepth(tree[c], d + 1)


def getDepth(node_number):
    return depths[node_number]


def showTree(root):
    for node in tree:
        type = ""
        if node.parent.number == -1:
            type = "root"
        elif len(node.child) == 0:
            type = "leaf"
        else:
            type = "internal node"

        print("node {0}: parent = {1}, depth = {2}, {3}, {4}".format(str(node.number), str(node.parent.number), str(depths[node.number]), type, node.child))


class Node():
    def __init__(self, number, parent, child):
        self.number = number
        self.parent = parent
        self.child = child


if __name__ == '__main__':
    main()

