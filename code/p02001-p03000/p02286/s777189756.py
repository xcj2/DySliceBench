class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None

# 根
parent_node = None    
    
# カウンター
counter = 0
        
def getRoot(u):
    while u.parent != None:
        u = u.parent
    return u


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


def rightRotate(u):
    # print("right")
    s = u.left
    u.left = s.right
    # 親の更新
    if u.left != None:
        u.left.parent = u
    
    s.right = u 
    # 親の更新
    s.parent = u.parent
    u.parent = s
    return s

def leftRotate(u):
    # print("left")
    s = u.right
    u.right = s.left
    # 親の更新
    if u.right != None:
        u.right.parent = u
    
    s.left = u
    # 親の更新
    s.parent = u.parent
    u.parent = s
    return s

        
def insert(u, key, priority):
    # print("insert 1")
    global parent_node
    global counter
    if u == None:
        s = Nodes[counter]
        # カウンターの増加
        counter += 1
        s.key = key
        s.priority = priority
        # 根のノードの更新
        if parent_node == None:
            parent_node = s
        return s
    
    if key == u.key:
        return u
    
    if key < u.key:
        u.left = insert(u.left, key, priority)
        # 親の更新
        u.left.parent = u
        if u.priority < u.left.priority:
            u = rightRotate(u)
    else:
        u.right = insert(u.right, key, priority)
        # 親の更新
        u.right.parent = u
        if u.priority < u.right.priority:
            u = leftRotate(u)
    
    return u
    

def delete(u, key):
    # print("delete")
    if u == None:
        return None
    if key < u.key:
        u.left = delete(u.left, key)
    elif key > u.key:
        u.right = delete(u.right, key)
    else:
        return _delete(u, key)
    return u


def _delete(u, key):
    # print("_delete")
    if u.left == None and u.right == None:
        return None
    elif u.left == None:
        u = leftRotate(u)
    elif u.right == None:
        u = rightRotate(u)
    else:
        if u.left.priority > u.right.priority:
            u = rightRotate(u)
        else:
            u = leftRotate(u)
    return delete(u, key)
    
    
n = int(input())

# メモリの確保
Nodes = []
for i in range(n):
    tmp_node = Node(0, 0)
    Nodes.append(tmp_node)



for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        key = int(cmd[1])
        priority = int(cmd[2])
        insert(parent_node, key, priority)
        # print("test in")
        # 根が変わる場合を考慮する。
        parent_node = getRoot(parent_node)
        # print("test out")
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
        
        # 根が変わる場合を考慮する。
        if parent_node.key != key:
            delete(parent_node, key)
            parent_node = getRoot(parent_node)
        elif parent_node.left != None:
            tmp_node = parent_node.left
            delete(parent_node, key)
            parent_node = getRoot(tmp_node)
        elif parent_node.right != None:
            tmp_node = parent_node.right
            delete(parent_node, key)
            parent_node = getRoot(tmp_node)
        else:
            delete(parent_node, key)
            parent_node = None
