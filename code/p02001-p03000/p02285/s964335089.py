class BinaryTree:
    def __init__(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent
        self.key = None
        self.root = False
        

def insert(T, z):
    global root
    
    y = -1
    try:
        x = root
    except:
        x = -1
        root = z
        T[z].root = True
    
    while x != -1:
        y = x
        if T[z].key < T[x].key:
            x = T[x].left
        else:
            x = T[x].right
    T[z].parent = y
    
    if y == -1:
        pass
    
    elif T[z].key < T[y].key:
        T[y].left = z
        
    else:
        T[y].right = z

def find(T, z, s):
    if s == -1:
        return [False, None]
        
    elif T[s].key == z:
        return [True, s]
        
    elif T[s].key < z:
        return find(T, z, T[s].right)
        
    else:
        return find(T, z, T[s].left)

def delete(T, z):
    global root
    z_has_left = T[z].left != -1
    z_has_right = T[z].right != -1
    
    
    if (not z_has_left) or (not z_has_right):
        y = z
    else:
        y = getsucsessor(T, z)


    if T[y].left != -1:
        x = T[y].left
    else:
        x = T[y].right
    
    if x != -1:
        T[x].parent = T[y].parent
    
    if T[y].root:
        T[x].root = True
        T[y].root = False
        root = x
    
    elif T[T[y].parent].left == y:
        T[T[y].parent].left = x
    else:
        T[T[y].parent].right = x
    
    T[z].key = T[y].key
    T[y] = BinaryTree(-1, -1, -1)

def getsucsessor(T, x):
    if T[x].right != -1:
        
        return getMinimum(T, T[x].right)
        
    else:
        y = T[x].parent
        while (y != -1) and (T[y].right == x):
            x = y
            y = T[y].parent
        return y

def getMinimum(T, x):
    while T[x].left != -1:
        x = T[x].left
    return x
        
    
def preParse(u):
    if u == -1:
        return 0
    print(" " + str(T[u].key), end="")
    preParse(T[u].left)
    preParse(T[u].right)

def inParse(u):
    if u == -1:
        return 0
    inParse(T[u].left)
    print(" " + str(T[u].key), end="")
    inParse(T[u].right)

m = int(input().rstrip())

z = 0
T = []
for _ in range(m):
    T.append(BinaryTree(-1, -1, -1))

for _ in range(m):
    command = input().rstrip()
    if command =="print":
        inParse(root)
        print()
        preParse(root)
        print()
    else:
        command, key = command.split(" ")
        key = int(key)
    
    
    if command == "insert":
        T[z].key = key
        insert(T, z)
        z += 1
        
    elif command == "find":
        if find(T, key, root)[0]:
            print("yes")
        else:
            print("no")
    
    elif command == "delete":
        x = find(T, key, root)[1]
        
        delete(T, x)
        


