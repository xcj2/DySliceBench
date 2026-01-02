class Node:
    def __init__(self, num=None, parent=None, left=None, right=None, type=None):
        self.num = num
        self.parent = parent
        self.left = left
        self.right = right
        self.type = type

    def __str__(self):
        return str(self.num)

def getType(node):
    if node.parent is None:
        return 'root'
    elif node.left is None and node.right is None:
        return 'leaf'
    else:
        return 'internal node'

def addNodeNumToResult (node, result):
    """
    Add node number to a list (converted to string)
    :param node: a node
    :param result: a list that stores result
    :return: Nothing
    """
    result.append(str(node.num))

def preParse(node, result):
    if node is None:
        return
    addNodeNumToResult(node, result)
    preParse(node.left, result)
    preParse(node.right, result)

def inParse(node, result):
    if node is None:
        return
    inParse(node.left, result)
    addNodeNumToResult(node, result)
    inParse(node.right, result)

def postParse(node, result):
    if node is None:
        return
    postParse(node.left, result)
    postParse(node.right, result)
    addNodeNumToResult(node, result)

# import sys
# sys.stdin = open('input.txt', 'r')

n = int(input())
nodes = []

# Initiate all nodes
for i in range(n):
    node = Node(i)
    nodes.append(node)

# Set parent, left and right from input
for i in range(n):
    num, leftNum, rightNum = map(int, input().split())
    node = nodes[num]
    if leftNum != -1:
        node.left = nodes[leftNum]
        node.left.parent = node
    if rightNum != -1:
        node.right = nodes[rightNum]
        node.right.parent = node

# Get root node
for node in nodes:
    node.type = getType(node)
    if node.type == 'root':
        root = node

result = []
preParse(root, result)
print('Preorder')
print('', end=' ')
print(' '.join(result))

result = []
inParse(root, result)
print('Inorder')
print('', end=' ')
print(' '.join(result))

result = []
postParse(root, result)
print('Postorder')
print('', end=' ')
print(' '.join(result))
