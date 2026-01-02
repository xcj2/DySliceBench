class Node:
    def __init__(self, parent, left, right):
        self.parent, self.left, self.right = parent, left, right

N = int(input())
T = [Node(None, None, None) for _ in range(N)]
for t in T:
    i, left, right = map(int, input().split())
    if left != -1:
        T[i].left = left
        T[left].parent = i
    if right != -1:
        T[i].right = right
        T[right].parent = i

def get_sibling(i):
    if T[i].parent == None:
        return -1
    if i != T[T[i].parent].left and T[T[i].parent].left != None:
        return T[T[i].parent].left
    if i != T[T[i].parent].right and T[T[i].parent].right != None:
        return T[T[i].parent].right
    return -1

def get_depth(i):
    depth = 0
    while T[i].parent != None:
        depth += 1
        i = T[i].parent
    return depth

def get_height(i):
    h1, h2 = 0, 0
    if T[i].left != None:
        h1 = get_height(T[i].left) + 1
    if T[i].right != None:
        h2 = get_height(T[i].right) + 1
    return max(h1, h2)

for i, t in enumerate(T):
    print('node {}:'.format(i), end=' ')
    parent = t.parent if t.parent != None else -1
    print('parent = {},'.format(parent), end=' ')
    sibling = get_sibling(i)
    print('sibling = {},'.format(sibling), end=' ')
    degree = 0
    if t.left != None:
        degree += 1
    if t.right != None:
        degree += 1
    print('degree = {},'.format(degree), end=' ')
    depth = get_depth(i)
    print('depth = {},'.format(depth), end=' ')
    height = get_height(i)
    print('height = {},'.format(height), end=' ')
    if t.parent == None:
        node = 'root'
    elif t.left == None and t.right == None:
        node = 'leaf'
    else:
        node = 'internal node'
    print(node)
