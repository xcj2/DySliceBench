class node():
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

root = None

def insert(r, z):
    global root

    y = None
    x = root

    while x != None:
        y = x

        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y

    if y == None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def Inorder_TreeWalk(node):
    if node is None:
        return

    Inorder_TreeWalk(node.left)
    print(" " + str(node.key), end="")
    Inorder_TreeWalk(node.right)

def Preorder_TreeWalk(node):
    if node is None:
            return
            
    print(" " + str(node.key), end="")
    Preorder_TreeWalk(node.left)
    Preorder_TreeWalk(node.right)

def Main():
    
    n = int(input())
    global root

    for i in range(n):
        inp = input().split()
        ope = inp[0]

        if ope == "insert":
            insert(root, node(int(inp[1]), None, None, None))

        elif ope == "print":
            Inorder_TreeWalk(root)
            print()
            Preorder_TreeWalk(root)
            print()
        else:
            pass
Main()
