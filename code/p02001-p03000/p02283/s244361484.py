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
        T[z].key = int(command.split(" ")[-1])
        insert(T, z)
        z += 1

