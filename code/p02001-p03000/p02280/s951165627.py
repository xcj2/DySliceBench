class Node:
    def __init__(self, num=None, parent=None, left=None, right=None, depth=None, height=None, sibling=None
                 , degree=None, type=None):
        self.num = num
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth
        self.height = height
        self.sibling = sibling
        self.degree = degree
        self.type = type

    def __str__(self):
        if self.parent is None:
            resParent = '-1'
        else:
            resParent = str(self.parent.num)

        if self.sibling is None:
            resSibling = '-1'
        else:
            resSibling = str(self.sibling.num)

        return 'node ' + str(self.num) + ': parent = ' + resParent + ', sibling = ' + resSibling \
               + ', degree = ' + str(self.degree) + ', depth = ' + str(self.depth) + ', height = ' + str(self.height) \
               + ', ' + self.type

def setDepth(node, depth):
    """
    :param node: Root node (in order to set height value to all nodes underneath
    :param depth: Depth of root node (=0)
    :return: nothing
    """
    if node == None:
        return
    node.depth = depth
    setDepth(node.left, depth+1)
    setDepth(node.right, depth+1)

def setHeight(node):
    """
    :param node: Root node (in order to set height value to all nodes underneath
    :return: height + set height value to all nodes underneatha
    """
    h1, h2 = 0, 0
    if node.left is not None:
        h1 = setHeight(node.left) + 1
    if node.right is not None:
        h2 = setHeight(node.right) + 1
    height = max(h1, h2)
    node.height = height
    return height

def getSibling(node):
    parent = node.parent
    if parent is None:
        return None
    elif parent.left != node and parent.left is not None:
        return parent.left
    elif parent.right != node and parent.right is not None:
        return parent.right
    return None

def getDegree(node):
    if node.left is None and node.right is None:
        return 0
    elif node.left is None or node.right is None:
        return 1
    else:
        return 2

def getType(node):
    if node.parent is None:
        return 'root'
    elif node.left is None and node.right is None:
        return 'leaf'
    else:
        return 'internal node'

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

for node in nodes:
    node.sibling = getSibling(node)
    node.degree = getDegree(node)
    node.type = getType(node)
    if node.type == 'root':
        root = node

setDepth(root, 0)
setHeight(root)

for node in nodes:
    print(node)

