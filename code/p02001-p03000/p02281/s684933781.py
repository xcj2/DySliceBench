import sys


class Node:
    def __init__(self):
        self.parent = self.left = self.right = None


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


def preorder(id):
    node = nodes[id]
    yield id
    if node.left is not None:
        yield from preorder(node.left)
    if node.right is not None:
        yield from preorder(node.right)


def inorder(id):
    node = nodes[id]
    if node.left is not None:
        yield from inorder(node.left)
    yield id
    if node.right is not None:
        yield from inorder(node.right)


def postorder(id):
    node = nodes[id]
    if node.left is not None:
        yield from postorder(node.left)
    if node.right is not None:
        yield from postorder(node.right)
    yield id


root_id = next(i for i, node in enumerate(nodes) if node.parent is None)
print('Preorder')
print(' ' + ' '.join(map(str, preorder(root_id))))
print('Inorder')
print(' ' + ' '.join(map(str, inorder(root_id))))
print('Postorder')
print(' ' + ' '.join(map(str, postorder(root_id))))

