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

    child = []
    if d[i][1] >= 0:
        child.append(d[i][1])
    if d[i][2] >= 0:
        child.append(d[i][2])

    new_node = node(i, parent, child, depth, type_t, sibling)
    t.append(new_node)
    sib = -1
    if len(child) == 1:
        add(t, d, child[0], i, depth + 1, sib)
    elif len(child) == 2:
        add(t, d, child[0], i, depth + 1, child[1])
        add(t, d, child[1], i, depth + 1, child[0])


def calc_height(t, i):
    if len(t[i].child) == 0:
        return 0
    max_h = -1
    for c in t[i].child:
        max_h = max(max_h, calc_height(t, c))
    return max_h + 1


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


for t in tree:
    print(f'node {t.id}: parent = {t.parent}, sibling = {t.sibling},'
          f' degree = {len(t.child)}, depth = {t.depth},'
          f' height = {t.height}, {t.type_t}')


