class Node():
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.key)
def inorder(r): ##r:root
    if (r.left != None):
        inorder(r.left)
    print(' ' + str(r.key), end ='')
    if (r.right != None):
        inorder(r.right)
def preorder(r):  ##r:root 
    print(" "+str(r.key), end ='')  ##preorder은 루트 쪽부터 print
    if (r.left != None):  ##left쪽으로 쭉감
        preorder(r.left) ##ns[i].left를 root로써 재귀함수!
    if (r.right != None):
        preorder(r.right) ##left다했으면 right으로도 똑같이 해줌 
root = None
def insert(z,root):
    y = None
    x = root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    
    if z.key < y.key:
        y.left = z
    else:
        y.right = z

def find(z,root):
    flag = 0
    while root != None:
        k = root.key
        if k==z:
            flag = 1
            break
        elif z>k:
            root = root.right
        elif z<k:
            root = root.left
    if flag:
        print("yes")
    else:
        print("no")
        
    

n = int(input())
command = str(input())
if command[0]=="i":
    root = Node(int(command[7:]))
else:
    print()
for i in range(n-1):
    com = str(input())
    if com[0] == "i":
        insert(Node(int(com[7:])),root)
    elif com[0]=="p":
        inorder(root)
        print()
        preorder(root)
        print()
    elif com[0] == "f":
        find(int(com[5:]),root)
    
