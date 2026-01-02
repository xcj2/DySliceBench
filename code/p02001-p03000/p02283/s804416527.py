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
            tmpParent = x
            if newNode.key < x.key:
                x = x.left
            else:
                x = x.right
        newNode.parent = tmpParent
        if newNode.key < tmpParent.key:
            tmpParent.left = newNode
        else:
            tmpParent.right = newNode

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
    result = []
    orderFunction(node, result)
    result = [i for i in map(str, result)]
    print(' ', end='')
    print(' '.join(result))
    

root = Node()
n = int(input())

for i in range(n):
    command = input()
    try:
        command, key = command.split()
        key = int(key)
        insert(key)
    except ValueError:
        printOrderedResult(root, inorder)
        printOrderedResult(root, preorder)
