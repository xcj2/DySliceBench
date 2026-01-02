class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

parent_node = None

        
def getParent():
    tmp_node = Nodes
    while Nodes.parent != None:
        tmp_node = tmp_node.parent
    return tmp_node    

def printPreorder(u):
    if u == None:
        return
    print(" ", u.key, sep="", end="")
    printPreorder(u.left)
    printPreorder(u.right)
    
def printInorder(u):
    if u == None:
        return
    printInorder(u.left)
    print(" ", u.key, sep="", end="")
    printInorder(u.right)

def find(u, num):
    while u != None and u.key != num:
        if num < u.key:
            u = u.left
        else:
            u = u.right
    if u != None:
        print("yes")
    else:
        print("no")

def getMinimum(u):
    while u.left != None:
        u = u.left
    return u

def getSuccessor(u):
    if u.right != None:
        return getMinimum(u.right)
    
    y = u.parent
    while y != None and u == y.right:
        u = y
        y = y.parent
    return y
        
def delete(u, num):
    while u != None and u.key != num:
        if num < u.key:
            u = u.left
        else:
            u = u.right
            
    y = None
    if u.left == None or u.right == None:
        y = u
    else:
        y = getSuccessor(u)
    
    x = None
    if y.left != None:
        x = y.left
    else:
        x = y.right
    
    if x != None:
        x.parent = y.parent
    
    if y.parent == None:
        parent_node = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    
    if y != u:
        u.key = y.key
    
n = int(input())

# メモリの確保
Nodes = []
for i in range(n):
    tmp_node = Node(0)
    Nodes.append(tmp_node)

for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        key = int(cmd[1])

        insert_node = Nodes[i]
        insert_node.key = key
        key_parent = None
        x = parent_node
            
        while x != None:
            key_parent = x
            if insert_node.key < x.key:
                x = x.left
            else:
                x = x.right
        insert_node.parent = key_parent
            
        if key_parent == None:
            parent_node = insert_node
        elif insert_node.key < key_parent.key:
            key_parent.left = insert_node
        else:
            key_parent.right = insert_node
    # プリント
    elif cmd[0] == 'print':
        printInorder(parent_node)
        print("")
        printPreorder(parent_node)
        print("")
    # サーチ
    elif cmd[0] == 'find':
        key = int(cmd[1])
        find(parent_node, key)
    # 削除
    else:
        key = int(cmd[1])
        delete(parent_node, key)
