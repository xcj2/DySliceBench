NIL = -1

class Node:
    def __init__(self, parent=NIL, left=NIL, right=NIL):
        self.parent = parent
        self.left = left
        self.right = right


def setDepth(tree, depthList, u, depth):
    if u == NIL:
        return
    depthList[u] = depth
    setDepth(tree, depthList, tree[u].left, depth + 1)
    setDepth(tree, depthList, tree[u].right, depth + 1)


def setHeight(tree, heightList, u):
    h1 = 0
    h2 = 0
    if tree[u].left != NIL:
        h1 = setHeight(tree, heightList, tree[u].left) + 1
    if tree[u].right != NIL:
        h2 = setHeight(tree, heightList, tree[u].right) + 1
    heightList[u] = max(h1, h2)
    return heightList[u]


def getSibling(tree, u):
    if tree[u].parent == NIL:
        return NIL
    if tree[tree[u].parent].left not in (u, NIL):
        return tree[tree[u].parent].left
    if tree[tree[u].parent].right not in (u, NIL):
        return tree[tree[u].parent].right
    return NIL


def printNode(tree, depthList, heightList, u):
    result = 'node %d: ' % u
    result += 'parent = %d, ' % tree[u].parent
    result += 'sibling = %d, ' % getSibling(tree, u)
    deg = 0
    if tree[u].left != NIL:
        deg += 1
    if tree[u].right != NIL:
        deg += 1
    result += 'degree = %d, ' % deg
    result += 'depth = %d, ' % depthList[u]
    result += 'height = %d, ' % heightList[u]

    if tree[u].parent == NIL:
        result += 'root'
    elif tree[u].left == NIL and tree[u].right == NIL:
        result += 'leaf'
    else:
        result += 'internal node'
    print(result)


n = int(input())
tree = [Node() for i in range(n)]

for i in range(n):
    value, left, right = [int(v) for v in input().split()]
    tree[value].left = left
    tree[value].right = right
    if left != NIL:
        tree[left].parent = value
    if right != NIL:
        tree[right].parent = value

root = 0
for i in range(n):
    if tree[i].parent == NIL:
        root = i
        break

depthList = [-1] * n
heightList = [-1] * n
setDepth(tree, depthList, root, 0)
setHeight(tree, heightList, root)
for i in range(n):
    printNode(tree, depthList, heightList, i)
