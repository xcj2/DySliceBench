
class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None


def rightRotate(t):
    s = t.left
    t.left = s.right
    s.right = t
    return s


def leftRotate(t):
    s = t.right
    t.right = s.left
    s.left = t
    return s


def insert(t, key, priority):
    if t is None:
        return Node(key, priority)
    if key == t.key:
        return t

    if key < t.key:
        t.left = insert(t.left, key, priority)
        if t.priority < t.left.priority:
            t = rightRotate(t)
    else:
        t.right = insert(t.right, key, priority)
        if t.priority < t.right.priority:
            t = leftRotate(t)

    return t


def delete(t, key):
    if t is None:
        return None
    if key < t.key:
        t.left = delete(t.left, key)
    elif key > t.key:
        t.right = delete(t.right, key)
    else:
        return _delete(t, key)
    return t


def _delete(t, key):
    if t.left is None and t.right is None:
        return None
    elif t.left is None:
        t = leftRotate(t)
    elif t.right is None:
        t = rightRotate(t)
    else:
        if t.left.priority > t.right.priority:
            t = rightRotate(t)
        else:
            t = leftRotate(t)
    return delete(t, key)


def find(t, key):
    if key == t.key:
        return t

    elif key < t.key:
        if t.left is not None:
            ret = find(t.left, key)
            if ret is not None:
                return ret
    else:
        if t.right is not None:
            ret = find(t.right, key)
            if ret is not None:
                return ret

    return None


def preorder(t, ret):
    ret.append(t.key)

    if t.left is not None:
        preorder(t.left, ret)

    if t.right is not None:
        preorder(t.right, ret)


def inorder(t, ret):
    if t.left is not None:
        inorder(t.left, ret)

    ret.append(t.key)

    if t.right is not None:
        inorder(t.right, ret)


def main():
    m = int(input())
    Treap = None
    for i in range(m):
        cmd, *v = input().split()
        if cmd == "print":
            print(" ", end="")
            inans = []
            inorder(Treap, inans)
            print(*inans)
            print(" ", end="")
            preans = []
            preorder(Treap, preans)
            print(*preans)
        elif cmd == "insert":
            k = int(v[0])
            p = int(v[1])
            Treap = insert(Treap, k, p)
        elif cmd == "find":
            z = int(v[0])
            if find(Treap, z) == None:
                print("no")
            else:
                print("yes")
        else:
            z = int(v[0])
            Treap = delete(Treap, z)


if __name__ == '__main__':
    main()

