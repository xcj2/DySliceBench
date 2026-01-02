class node:
    def __init__(self,key,pri,left=None,right=None):
        self.left = left
        self.right = right
        self.key = key
        self.pri = pri

def insert(n,key,pri):
    if(n == None):
        return node(key,pri)
    if(key == n.key):
        return n
    if(key < n.key):
        n.left = insert(n.left, key, pri)
        if(n.pri < n.left.pri):
            n = rightRotate(n)
    else:
        n.right = insert(n.right, key, pri)
        if(n.pri < n.right.pri):
            n = leftRotate(n)
    return n

def rightRotate(n):
    child = n.left
    swapL,swapR,swapK,swapP = child.left,child.right,child.key,child.pri
    n.left = swapR
    n = node(swapK,swapP,swapL,n)
    return n

def leftRotate(n):
    child = n.right
    swapL,swapR,swapK,swapP = child.left,child.right,child.key,child.pri
    n.right = swapL
    n = node(swapK,swapP,n,swapR)
    return n

def find(n,key):
    if(n == None):
        return None
    elif(n.key == key):
        return n
    elif(n.key > key):
        return find(n.left,key)
    else:
        return find(n.right,key)

def delete(n, key):
    if(n == None):
        return None
    if(key < n.key):
        n.left = delete(n.left, key)
    elif(key > n.key):
        n.right = delete(n.right, key)
    else:
        return _delete(n, key)
    return n

def _delete(n, key):
    if(n.left == None and n.right == None):
        return None
    elif(n.left == None):
        n = leftRotate(n)
    elif(n.right == None):
        n = rightRotate(n)
    else:
        if(n.left.pri > n.right.pri):
            n = rightRotate(n)
        else:
            n = leftRotate(n)
    return delete(n, key)

def inorder(n):
    if(n==None):
        return
    if(n.left != None):
        inorder(n.left)
    print(" "+str(n.key), end='')
    if(n.right != None):
        inorder(n.right)

def preorder(n):
    if(n==None):
        return
    print(" "+str(n.key), end='')
    if(n.left != None):
        preorder(n.left)
    if(n.right != None):
        preorder(n.right)

op_num=(int)(input())
root = None
for i in range(op_num):
    items = input().split()
    if(items[0] == "insert"):
        root = insert(root,(int)(items[1]),(int)(items[2]))
    elif(items[0] == "delete"):
        root = delete(root,(int)(items[1]))
    elif(items[0] == "find"):
        res = find(root,(int)(items[1]))
        if(res == None):
            print("no")
        else:
            print("yes")
    else:
        inorder(root)
        print("")
        preorder(root)
        print("")

