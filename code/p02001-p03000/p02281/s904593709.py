class BinTree():
    def __init__(self):
        self.parent = -1
        self.left, self.right = -1, -1
        self.sib = -1
        self.dep, self.deg, self.h = 0, 0, 0
        self.state = "internal node"

    def set_node(self, nid, l, r):
        global root
        root -= {l, r}
        self.left, self.right = l, r
        self.deg = (l != -1) + (r != -1)
        if l != -1:
            left = trees[l]
            left.parent = nid
            left.sib = r
        if r != -1:
            right = trees[r]
            right.parent = nid
            right.sib = l

    def set_param(self):
        if self.parent != -1:
            self.dep = trees[self.parent].dep + 1
        if self.deg == 0:
            self.state = "leaf"
        if self.left != -1:
            left = trees[self.left]
            left.set_param()
            self.h = left.h + 1
        if self.right != -1:
            right = trees[self.right]
            right.set_param()
            if self.h <= right.h:
                self.h = right.h + 1
        if self.parent == -1:
            self.state = "root"

def pre_walk(nid):
    tree = trees[nid]
    print(" {}".format(nid), end="")
    if tree.left != -1:
        pre_walk(tree.left)
    if tree.right != -1:
        pre_walk(tree.right)

def preoder(root):
    print("Preorder")
    pre_walk(root)
    print()

def in_walk(nid):
    tree = trees[nid]
    if tree.left != -1:
        in_walk(tree.left)
    print(" {}".format(nid), end="")
    if tree.right != -1:
        in_walk(tree.right)

def inorder(root):
    print("Inorder")
    in_walk(root)
    print()

def post_walk(nid):
    tree = trees[nid]
    if tree.left != -1:
        post_walk(tree.left)
    if tree.right != -1:
        post_walk(tree.right)
    print(" {}".format(nid), end="")

def postorder(root):
    print("Postorder")
    post_walk(root)
    print()

n = int(input())
trees = [BinTree() for _ in range(n)]
root = set(range(n))
for _ in range(n):
    inp = list(map(int, input().split()))
    trees[inp[0]].set_node(*inp)
root = root.pop()
trees[root].set_param()
preoder(root)
inorder(root)
postorder(root)