class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self

def find_root(node):
    if node.parent == node:
        return node

    else:
        node.parent = find_root(node.parent)
        return node.parent

def unite(x, y):
    x_root = find_root(x)
    y_root = find_root(y)
    if x_root == y_root:
        return
    else:
        y_root.parent = x_root

def same(x, y):
    if find_root(x) == find_root(y):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    n, q = map(int, input().split())

    nodeset = []
    for i in range(n):
        nodeset.append(Node(i))

    for i in range(q):  
        com, x, y = map(int, input().split())
        x_node = nodeset[x]
        y_node = nodeset[y]
        if com == 0:
            unite(x_node, y_node)
        else:
            same(x_node, y_node)
