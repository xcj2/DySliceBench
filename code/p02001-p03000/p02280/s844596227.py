import sys


class Node:
    def __init__(self):
        self.parent = self.left = self.right = None
        self.height = self.depth = None


n = int(sys.stdin.readline())

nodes = [Node() for _ in range(n)]

for _ in range(n):
    id, left, right = map(int, sys.stdin.readline().split())
    if left != -1:
        nodes[id].left = left
        nodes[left].parent = id
    if right != -1:
        nodes[id].right = right
        nodes[right].parent = id


def set_height(id):
    node = nodes[id]
    height = max(
        -1 if child is None else set_height(child)
        for child in (node.left, node.right)
    ) + 1
    node.height = height
    return height


def set_depth(id, depth):
    node = nodes[id]
    node.depth = depth
    for child in (node.left, node.right):
        if child is not None:
            set_depth(child, depth + 1)


root_id = next(i for i, node in enumerate(nodes) if node.parent is None)
set_height(root_id)
set_depth(root_id, 0)

for id, node in enumerate(nodes):
    sibling = -1
    if node.parent is not None:
        parent = nodes[node.parent]
        sibling = parent.right if parent.left == id else parent.left
        if sibling is None:
            sibling = -1

    node_type = 'internal node'
    if node.parent is None:
        node_type = 'root'
    elif node.left is None and node.right is None:
        node_type = 'leaf'

    print(
        (
            'node %d: parent = %d, sibling = %d, ' +
            'degree = %d, depth = %d, height = %d, %s'
        ) % (
            id,
            -1 if node.parent is None else node.parent,
            sibling,
            sum(child is not None for child in (node.left, node.right)),
            node.depth,
            node.height,
            node_type
        ))

