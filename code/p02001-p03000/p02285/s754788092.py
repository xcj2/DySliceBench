class node():
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

root = None

def insert(z):
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

def find(key):
    
    x = root
    answer = None

    while x != None:

        if key == x.key:
            answer = x
            break

        if key < x.key:
            x = x.left
        else:
            x = x.right
    
    return answer
    
def delete(key):
    z = find(key)

    if z.left == None and z.right == None:
        if key < z.parent.key:
            z.parent.left = None
        else:
            z.parent.right = None
    
    elif z.left != None and z.right == None :
        if z.key < z.parent.key:
            z.parent.left = z.left
        else:
            z.parent.right = z.left
        
        z.left.parent = z.parent
    
    elif z.left == None and z.right != None :
        if z.key < z.parent.key:
            z.parent.left = z.right
        else:
            z.parent.right = z.right
        
        z.right.parent = z.parent

    elif z.left != None and z.right != None:
        next_node = z.right

        while next_node.left != None:
            next_node = next_node.left

        new_key = next_node.key
        delete(new_key)

        z.key = new_key

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
    global root
    n = int(input())
    
    for i in range(n):
        inp = input().split()
        ope = inp[0]

        if ope == "insert":
            insert(node(int(inp[1]), None, None, None))
        
        elif ope == "find":
            target = find(int(inp[1]))

            if target != None:
                print("yes")
            else:
                print("no")

        elif ope == "delete":
            delete(int(inp[1]))

        elif ope == "print":
            Inorder_TreeWalk(root)
            print()
            Preorder_TreeWalk(root)
            print()
Main()
