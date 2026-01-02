
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def insert(T, z):
    y = None
    x = T
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y

    if y is None:
        T = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

    return T


def preorder(T, ret):
    ret.append(T.key)

    if T.left is not None:
        preorder(T.left, ret)

    if T.right is not None:
        preorder(T.right, ret)


def inorder(T, ret):
    if T.left is not None:
        inorder(T.left, ret)

    ret.append(T.key)

    if T.right is not None:
        inorder(T.right, ret)


def main():
    m = int(input())
    Tree = None
    for i in range(m):
        cmd, *v = input().split()
        if cmd == "print":
            print(" ", end="")
            inans = []
            inorder(Tree, inans)
            print(*inans)
            print(" ", end="")
            preans = []
            preorder(Tree, preans)
            print(*preans)
        else:
            z = int(v[0])
            znode = Node(z)
            Tree = insert(Tree, znode)


if __name__ == '__main__':
    main()

