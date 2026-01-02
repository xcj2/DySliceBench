class Node:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right
        self.parent = -1
        self.sibling = -1
        self.degree = 0
        self.depth = 0
        self.height = 0
        self.type = ""

    def __str__(self):
        if self.parent == -1:
            self.type = "root"
        elif self.degree == 0:
            self.type = "leaf"
        else:
            self.type = "internal node"
        return "node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(
            self.node, self.parent, self.sibling, self.degree, self.depth, self.height, self.type)


preOrder = None
inOrder = None
postOrder = None


def dfs(tree, v, p, d, s):
    global preOrder, inOrder, postOrder
    preOrder.append(v)
    tree[v].parent = p
    tree[v].depth = d
    tree[v].sibling = s
    maxheight = 0
    if tree[v].left != -1:
        tree[v].degree += 1
        maxheight = max(
            maxheight, dfs(
                tree, tree[v].left, v, d + 1, tree[v].right))
    inOrder.append(v)
    if tree[v].right != -1:
        tree[v].degree += 1
        maxheight = max(
            maxheight, dfs(
                tree, tree[v].right, v, d + 1, tree[v].left))
    postOrder.append(v)
    if tree[v].left == tree[v].right:
        tree[v].height = 0
        return 0
    tree[v].height = maxheight + 1
    return tree[v].height


def resolve():
    global preOrder, inOrder, postOrder
    preOrder, inOrder, postOrder = [], [], []
    n = int(input())
    tree = [None for i in range(n)]
    V = [list(map(int, input().split())) for _ in range(n)]
    hasChild = set()
    childrens = set()
    for a, left, right in V:
        tree[a] = Node(a, left, right)
        if left != right:
            hasChild.add(a)
            childrens.add(left)
            childrens.add(right)
    root = hasChild - childrens
    if len(root) > 0:
        root = root.pop()
    else:
        root = 0
    dfs(tree, root, -1, 0, -1)
    print("Preorder")
    print("", *preOrder)
    print("Inorder")
    print("", *inOrder)
    print("Postorder")
    print("", *postOrder)


resolve()

