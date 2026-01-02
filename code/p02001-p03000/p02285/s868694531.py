

class Node:
    def __init__(self, key):
        self.parent = None
        self.right = None
        self.left = None
        self.key = key

def insert(root, z):
    y = None
    x = None
    if root != None:
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

def find(x, k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x
    
def delete(root, z):
    if z.left == None or z.right == None:
        y = z
    else:
        y = getSuccessor(z)
    
    if y.left != None:
        x = y.left
    else:
        x = y.right
        
    if x != None:
        x.parent = y.parent
    
    if y.parent == None:
        root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    
    if y != z:
        z.key = y.key

def getSuccessor(x):
    if x.right != None:
        return getMinimum(x.right)
    y = x.parent
    while y != None and x == y.right:
        x = y
        y = y.parent
    return y

def getMinimum(x):
    while x.left != None:
        x = x.left
    return x
    
def printInOrder(z):
    if z == None:
        return
    if z.left != None:
        printInOrder(z.left)
    inorder.append(str(z.key))
    #print(z.key, end = " ")
    if z.right != None:
        printInOrder(z.right)
        
def printPreOrder(z):
    if z == None:
        return
    #print(z.key, end = " ")
    preorder.append(str(z.key))
    if z.left != None:
        printPreOrder(z.left)
    if z.right != None:
        printPreOrder(z.right)

root = None


n = int(input())
for i in range(n):
    command = input()
    if command[0] == "i":
        com,num = command.split()
        z = Node(int(num))
        insert(root, z)
        if root == None:
            root = z
    elif command[0] == "f":
        com,num = command.split()
        z = Node(int(num))
        x = find(root, int(z.key))
        if x != None:
            print("yes")
        else:
            print("no")
    
    elif command[0] =="d":
        com,num = command.split()
        z = Node(int(num))
        delete(root, find(root, int(z.key)))
    

    else:
        inorder = []
        printInOrder(root)
        print(" ", end = "")
        print(' '.join(inorder))
        preorder = []
        printPreOrder(root)
        print(" ", end = "")
        print(' '.join(preorder))





