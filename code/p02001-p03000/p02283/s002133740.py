NIL = None
class Tree:
    def __init__(self, key = None):
        self.key = key
        self.p = NIL
        self.left = NIL
        self.right = NIL
n = int(input())
tree = {"root":NIL}
def insert(T, z):
    y = NIL
    x = T["root"]
    while x != NIL:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == NIL:
        T["root"] = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
def preorder_tree_walk(T):
    print(f" {T.key}", end="")
    if T.left != NIL:
        preorder_tree_walk(T.left)
    if T.right != NIL:
        preorder_tree_walk(T.right)
def inorder_tree_walk(T):
    if T.left != NIL:
        inorder_tree_walk(T.left)
    print(f" {T.key}", end="")
    if T.right != NIL:
        inorder_tree_walk(T.right)
for _ in range(n):
    ss = input()
    if ss[0] == "i":
        s, v = ss.split()
        insert(tree, Tree(int(v)))
    else:
        inorder_tree_walk(tree["root"])
        print()
        preorder_tree_walk(tree["root"])
        print()

