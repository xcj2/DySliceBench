class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        
        
def insert(root, add):
    parent = None
    pCandidate = root
    while pCandidate is not None:
        parent = pCandidate
        if add.key < pCandidate.key:
            pCandidate = pCandidate.left
        else:
            pCandidate = pCandidate.right
    add.p = parent
    
    if parent is None:
        root = add
    elif add.key < parent.key:
        parent.left = add
    else:
        parent.right = add
    return root

def inorderTreeWalk(node):
    if node.left is not None:
        inorderTreeWalk(node.left)
    print(" {0}".format(node.key), end="")
    if node.right is not None:
        inorderTreeWalk(node.right)
        
def preorderTreeWalk(node):
    print(" {0}".format(node.key), end="")
    if node.left is not None:
        preorderTreeWalk(node.left)
    if node.right is not None:
        preorderTreeWalk(node.right)

n = int(input())
root = None
for i in range(n):
    line = input().split()
    if line[0] == "insert":
        root = insert(root, Node(int(line[1])))
    else:
        inorderTreeWalk(root)
        print()
        preorderTreeWalk(root)
        print()