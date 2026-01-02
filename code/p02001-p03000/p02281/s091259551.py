n = int(input())
tree = [None] * n
root = set(range(n))


def preorder(i):
    if i == -1: return
    (l, r) = tree[i]
    yield i
    for v in preorder(l): yield v
    for v in preorder(r): yield v


def inorder(i):
    if i == -1: return
    (l, r) = tree[i]
    for v in inorder(l): yield v
    yield i
    for v in inorder(r): yield v


def postorder(i):
    if i == -1: return
    (l, r) = tree[i]
    for v in postorder(l): yield v
    for v in postorder(r): yield v
    yield i


while n:
    i, l, r = list(map(int, input().split()))
    tree[i] = (l, r)
    root -= {l, r}
    n -= 1

root_node = root.pop()

for name, func in (('Preorder', preorder), ('Inorder', inorder), ('Postorder', postorder)):
    print(name)
    print(' ', end='')
    print(*func(root_node))