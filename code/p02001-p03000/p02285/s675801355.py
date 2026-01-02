import sys

class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

def insert(key):
    global root
    # The first node
    if root.key is None:
        root.key = key
        return
    # The second note and so forth
    else:
        newNode = Node(key)
        x = root
        while x is not None:
            tmpParent = x # parent 候補として保持
            if newNode.key < x.key:
                x = x.left
            else:
                x = x.right
        newNode.parent = tmpParent
        if newNode.key < tmpParent.key:
            tmpParent.left = newNode
        else:
            tmpParent.right = newNode

def find(key):
    """
    Find a node with the key (x: a node for search)
    :param key: Key to search
    :return: A node that has the key. Returns None if there is no match,
    """
    global root
    x = root
    while x is not None and x.key != key:
        if key < x.key:
            x = x.left
        else:
            x = x.right
    return x

def delete(key):
    global root
    z = find(key)

    if z.left is None or z.right is None:
        nodeToDelete = z
    else:
        nodeToDelete = getSuccessor(z)

    # x = nodeToDelete の子
    if nodeToDelete.left is not None:
        x = nodeToDelete.left
    else:
        x = nodeToDelete.right

    if x is not None:
        x.parent = nodeToDelete.parent

    if nodeToDelete.parent is None:
        root = x
    elif nodeToDelete == nodeToDelete.parent.left:
        nodeToDelete.parent.left = x
    else:
        nodeToDelete.parent.right = x

    if nodeToDelete != z:
        z.key = nodeToDelete.key

    # if x.left is None and x.right is None: # x が子を持たないとき
    #     if x.parent.left == x:
    #         x.parent.left = None
    #     else:
    #         x.parent.right = None
    # elif x.left is None or x.right is None: # x が 1 つだけ子を持つとき
    #     if x.left is not None:
    #         child = x.left
    #     else:
    #         child = x.right
    #     if x.parent.left == x:
    #         x.parent.left = child
    #     else:
    #         x.parent.right = child
    #     child.parent = x.parent
    # else: # x が 2 つ子を持つとき
    #     y = getSuccessor(x)
    #     delete(y.key)
    #     x.key = y.key

def getSuccessor(node):
    """
    node の次節点 (中間巡回で次に来る node を返す
    """
    if node.right is not None:
        return getMinimum(node.right)
    y = node.parent
    while y is not None and node == y.right:
        node = y
        y = y.parent
    return y

def getMinimum(node):
    while node.left is not None:
        node = node.left
    return node

def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.key)
    inorder(node.right, result)

def preorder(node, result):
    if node is None:
        return
    result.append(node.key)
    preorder(node.left, result)
    preorder(node.right, result)

def printOrderedResult(node, orderFunction):
    """
    :param node: node (root)
    :param orderFunction: inorder or preorder (function)
    :return: nothing
    """
    result = []
    orderFunction(node, result)
    result = [i for i in map(str, result)]
    print(' ', end='')
    print(' '.join(result))


# sys.stdin = open('input.txt')

root = Node()
n = int(input())

for i in range(n):
    command = input()
    try:
        command, key = command.split()
        key = int(key)
        if command == 'insert':
            insert(key)
        elif command == 'find':
            if find(key) is None:
                print('no')
            else:
                print('yes')
        elif command == 'delete':
            delete(key)
    except ValueError: # command == 'print'
        printOrderedResult(root, inorder)
        printOrderedResult(root, preorder)
