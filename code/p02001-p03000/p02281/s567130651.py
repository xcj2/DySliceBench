class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None
        self.parent = None

    def getId(self):
        return self.id

    def setRight(self, right):
        self.right = right

    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left

    def setParent(self, parent):
        self.parent = parent

    def isRoot(self):
        return self.parent is None

    def preorder(self):
        print('', self.id, end='')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print('', self.id, end='')
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print('', self.id, end='')

    def printInfo(self):
        if self.left is None:
            left = -1
        else:
            left = self.left.getId()
        if self.right is None:
            right = -1
        else:
            right = self.right.getId()
        print("{} {} {}".format(self.id, left, right))

n = int(input())

nodes = []

for i in range(n):
    nodes.append(Node(i))

for i in range(n):
    id, left, right = map(int, input().split())
    if left != -1:
        nodes[id].setLeft(nodes[left])
        nodes[left].setParent(nodes[id])
    if right != -1:
        nodes[id].setRight(nodes[right])
        nodes[right].setParent(nodes[id])

def getRootNode(nodes):
    for e in nodes:
        if e.isRoot():
            return e
    return None

def getLeftNode(nodes):
    node = getRootNode(nodes)
    while True:
        left = node.getLeft()
        if left is not None:
            node = left
        else:
            return node
    return None

def preorder(nodes):
    print('Preorder')
    root = getRootNode(nodes)
    root.preorder()
    print('')

def inorder(nodes):
    print('Inorder')
    root = getRootNode(nodes)
    root.inorder()
    print('')

def postorder(nodes):
    print('Postorder')
    root = getRootNode(nodes)
    root.postorder()
    print('')

preorder(nodes)
inorder(nodes)
postorder(nodes)

