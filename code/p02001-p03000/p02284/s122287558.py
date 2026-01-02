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
    Find a node with the key
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
    except ValueError: # command == 'print'
        printOrderedResult(root, inorder)
        printOrderedResult(root, preorder)
