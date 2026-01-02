
class Node:
    id = None
    parent = None
    left = None
    right = None
    sibling = -1
    depth = None
    height = None

    def __str__(self):
        degree = None
        _type = None

        return 'node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(self.id, self.parent, self.sibling, self.get_degree(), self.depth, self.height, self.get_type())

    def get_degree(self):
        degree = 0
        if self.left is not None:
            degree += 1
        if self.right is not None:
            degree += 1
        return degree

    def get_type(self):
        if self.parent == -1:
            return 'root'
        if self.get_degree() == 0:
            return 'leaf'
        else:
            return 'internal node'


def set_depth(node_id, depth):
    if node_id is None:
        return

    global T
    T[node_id].depth = depth
    set_depth(T[node_id].left, depth + 1)
    set_depth(T[node_id].right, depth + 1)


def set_height(node_id):
    global T

    h1, h2 = 0, 0
    if T[node_id].left is not None:
        h1 = set_height(T[node_id].left) + 1
    if T[node_id].right is not None:
        h2 = set_height(T[node_id].right) + 1

    T[node_id].height = max(h1, h2)

    return max(h1, h2)


def pre_order(node_id, _order):
    if node_id is None:
        return

    global T
    _order.append(node_id)
    pre_order(T[node_id].left, _order)
    pre_order(T[node_id].right, _order)


def in_order(node_id, _order):
    if node_id is None:
        return

    global T
    in_order(T[node_id].left, _order)
    _order.append(node_id)
    in_order(T[node_id].right, _order)


def post_order(node_id, _order):
    if node_id is None:
        return

    global T
    post_order(T[node_id].left, _order)
    post_order(T[node_id].right, _order)
    _order.append(node_id)


n = int(input())
T = []
root = 0

for i in range(n):
    T.append(Node())

for i in range(n):
    _ = list(map(int, input().split()))
    _id = _[0]
    left = _[1]
    right = _[2]
    if left == -1:
        left = None
    if right == -1:
        right = None

    T[_id].id = _id
    T[_id].left = left
    T[_id].right = right

    if left is not None:
        T[left].parent = _id
    if right is not None:
        T[right].parent = _id

    if left is not None and right is not None:
        T[left].sibling = right
        T[right].sibling = left

for i in range(n):
    if T[i].parent is None:
        T[i].parent = -1
        root = i
        break

set_depth(root, 0)
set_height(root)

# for i in range(n):
#     print(T[i])

order = []
print('Preorder')
pre_order(root, order)
print(' ' + ' '.join(map(str, order)))

order = []
print('Inorder')
in_order(root, order)
print(' ' + ' '.join(map(str, order)))

order = []
print('Postorder')
post_order(root, order)
print(' ' + ' '.join(map(str, order)))

