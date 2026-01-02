class node():
    def __init__(self, id, parent, child, depth, type_t, sibling, height=0):
        self.id = id
        self.parent = parent
        self.child = child
        self.depth = depth
        self.type_t = type_t
        self.sibling = sibling
        self.height = height


def add(t, d, i, parent, depth, sibling):
    type_t = 'internal node'
    if d[i][1] == -1 and d[i][2] == -1:
        type_t = 'leaf'
    if depth == 0:
        type_t = 'root'
    child = d[i][1:]
    new_node = node(i, parent, child, depth, type_t, sibling)
    t.append(new_node)
    if child[0] >= 0:
        sib = child[1] if child[1] >= 0 else -1
        add(t, d, child[0], i, depth + 1, sib)
    if child[1] >= 0:
        sib = child[0] if child[0] >= 0 else -1
        add(t, d, child[1], i, depth + 1, sib)


def calc_height(t, i):
    if t[i].child[0] == -1 and t[i].child[1] == -1:
        return 0
    max_h = -1
    if t[i].child[0] >= 0:
        max_h = max(max_h, calc_height(t, t[i].child[0]))
    if t[i].child[1] >= 0:
        max_h = max(max_h, calc_height(t, t[i].child[1]))
    return max_h + 1

def preorder(t, a, i):
    l, r = -1, -1
    l = t[i].child[0]
    r = t[i].child[1]
    a.append(i)
    if not l == -1:
        preorder(t, a, l)
    if not r == -1:
        preorder(t, a, r)


def inorder(t, a, i):
    l, r = -1, -1
    l = t[i].child[0]
    r = t[i].child[1]
    if not l == -1:
        inorder(t, a, l)
    a.append(i)
    if not r == -1:
        inorder(t, a, r)


def postorder(t, a, i):
    l, r = -1, -1
    l = t[i].child[0]
    r = t[i].child[1]
    if not l == -1:
        postorder(t, a, l)
    if not r == -1:
        postorder(t, a, r)
    a.append(i)

N = int(input())
tree = []
data = [[] for i in range(N)]
for i in range(N):
    data[i] = [int(i) for i in input().split()]

data.sort(key=lambda x: x[0])
root = [True for i in range(N)]
for d in data:
    for c in d[1:]:
        if c == -1:
            continue
        root[c] = False

root_index = root.index(True)
add(tree, data, root_index, -1, 0, -1)

tree.sort(key=lambda x: x.id)

for i in range(N):
    h = calc_height(tree, i)
    tree[i].height = h

a = []
preorder(tree, a, root_index)
print('Preorder')
print('', ' '.join(map(str, a)))
a = []
inorder(tree, a, root_index)
print('Inorder')
print('', ' '.join(map(str, a)))
a = []
postorder(tree, a, root_index)
print('Postorder')
print('', ' '.join(map(str, a)))

