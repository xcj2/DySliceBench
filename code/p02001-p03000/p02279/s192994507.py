class Node:
    def __init__(self, p, l, r):
        self.p, self.l, self.r = p, l, r

N = int(input())
T = [Node(None, None, None) for _ in range(N)]

def get_depth(i):
    depth = 0
    while T[i].p != None:
        depth += 1
        i = T[i].p
    return depth

def get_children(i):
    children = []
    child = T[i].l
    while child != None:
        children.append(child)
        child = T[child].r
    return children

for _ in range(N):
    node, num, *children = map(int, input().split())
    if len(children) > 0:
        T[node].l = children[0]
        for i, child in enumerate(children):
            if len(children) - 1 < i + 1:
                break
            T[child].r = children[i + 1]
        for child in children:
            T[child].p = node

for i, t in enumerate(T):
    parent = t.p if t.p != None else -1
    depth = get_depth(i)
    if t.p == None:
        node = 'root'
    elif t.l == None:
        node = 'leaf'
    else:
        node = 'internal node'
    children = get_children(i)
    print('node {}:'.format(i), end=' ')
    print('parent = {},'.format(parent), end=' ')
    print('depth = {},'.format(depth), end=' ')
    print('{},'.format(node), end=' ')
    print(children)
