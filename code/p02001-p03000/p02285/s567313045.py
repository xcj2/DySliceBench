
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


def find(T, key):
    if key == T.key:
        return T

    elif key < T.key:
        if T.left is not None:
            ret = find(T.left, key)
            if ret is not None:
                return ret
    else:
        if T.right is not None:
            ret = find(T.right, key)
            if ret is not None:
                return ret

    return None


def delete(T, key):
    if T is None:
        return None
    if key < T.key:
        delete(T.left, key)
    elif key > T.key:
        delete(T.right, key)
    else:
        _delete(T, key)


def _delete(T, key):
    parent = T.parent
    if T.left is None and T.right is None:
        if parent.left == T:
            parent.left = None
        else:
            parent.right = None
        T = None
    elif T.left is None or T.right is None:
        if parent.left == T:
            if T.left:
                parent.left = T.left
                T.left.parent = parent
            else:
                parent.left = T.right
                T.right.parent = parent
        else:
            if T.left:
                parent.right = T.left
                T.left.parent = parent
            else:
                parent.right = T.right
                T.right.parent = parent
        T = None
    else:
        nextnode = T.right
        while nextnode.left:
            nextnode = nextnode.left
        T.key = nextnode.key
        delete(nextnode, nextnode.key)


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
        elif cmd == "insert":
            z = int(v[0])
            znode = Node(z)
            Tree = insert(Tree, znode)
        elif cmd == "find":
            z = int(v[0])
            if find(Tree, z) == None:
                print("no")
            else:
                print("yes")
        else:
            z = int(v[0])
            delete(Tree, z)


if __name__ == '__main__':
    main()

