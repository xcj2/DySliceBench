def find(x):
    if tree[x] < 0:
        return x
    tree[x] = find(tree[x])
    return tree[x]


def unite(x, y):
    x_position = find(x)
    y_position = find(y)
    if x_position == y_position:
        return True
    if y_position < x_position:
        x_position, y_position = y_position, x_position
    tree[x_position] += tree[y_position]
    tree[y_position] = x_position
    return False


def same(x, y):
    if find(x) == find(y):
        print(1)
    else:
        print(0)


n, q = map(int, input().split())
tree = [-1] * n
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        unite(x, y)
    if com == 1:
        same(x, y)