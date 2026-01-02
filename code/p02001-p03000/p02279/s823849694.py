import sys

TYPE_ROOT = 0
TYPE_NODE = 1
TYPE_LEAF = 2


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = []
        self.type = None
        self.depth = 0


def set_depth(node, depth):
    node.depth = depth
    for child in node.children:
        set_depth(child, depth + 1)


nodes = {}


def get_node(id):
    if id in nodes:
        return nodes[id]
    node = Node(id)
    nodes[id] = node
    return node


n = int(sys.stdin.readline())
for _ in range(n):
    id, k, *children = map(int, sys.stdin.readline().split())
    node = get_node(id)
    for cid in children:
        child = get_node(cid)
        child.parent = node
        node.children.append(child)
    node.type = TYPE_NODE if node.children else TYPE_LEAF

root = next(node for node in nodes.values() if not node.parent)
root.type = TYPE_ROOT
set_depth(root, 0)


for _, node in sorted(nodes.items()):
    print('node %d: parent = %d, depth = %d, %s, [%s]' % (
        node.id,
        node.parent.id if node.parent else -1,
        node.depth,
        ['root', 'internal node', 'leaf'][node.type],
        ', '.join(str(child.id) for child in node.children)
    ))

