nodes = None


class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def insert(z):
    global nodes
    y = None
    x = nodes

    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right

    z.parent = y

    if y is None:
        nodes = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def find(node, key):
    # if node is None:
    #     return "no"
    #
    # if node.key == key:
    #     return "yes"
    # elif node.key > key:
    #     return find(node.left, key)
    # else:
    #     return find(node.right, key)
    while node is not None and node.key != key:
        if node.key > key:
            node = node.left
        else:
            node = node.right

    if node is None:
        return "no"
    if node.key == key:
        return "yes"
    raise AssertionError()


def get_inorder(inorder, node):
    if node.left is not None:
        get_inorder(inorder, node.left)
    inorder.append(node.key)
    if node.right is not None:
        get_inorder(inorder, node.right)
    return inorder


def get_preorder(preorder, node):
    preorder.append(node.key)
    if node.left is not None:
        get_preorder(preorder, node.left)
    if node.right is not None:
        get_preorder(preorder, node.right)
    return preorder


def p(node):
    print("", " ".join([str(i) for i in get_inorder([], node)]))
    print("", " ".join([str(i) for i in get_preorder([], node)]))


n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == "insert":
        key = int(s[1])
        insert(Node(key=key))
    elif s[0] == "find":
        key = int(s[1])
        print(find(nodes, key))
    else:
        p(nodes)

