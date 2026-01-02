import sys

class Node():
    #key = ตัว z เอง และตัวด้านซ้ายด้านขวา
    __slots__ = ['key', 'left', 'right']
    def __init__(self, key):
        self.key = key
        self.left, self.right = None, None
        
    def __str__(self):
        return self.key

root = None
#z คือรับเลขเข้ามาว่าจะ insert ค่าไหน
def insert(z):
    global root
    x, y = root, None
    #ทำการ update ค่า y ว่าตัวไหนเป็น root ต่อไป โดยมาเทียบกับ root ว่าจะลงซ้ายหรือขวา
    while x:
        y = x
        if z < x.key:
            x = x.left
        else:
            x = x.right
    
    if y == None:
       #ทำการ update ค่า y ให้ อีกที ว่าอะไรเป็น left เป็น right 
        root = Node(z)
    elif z < y.key:
        y.left = Node(z)
    else:
        y.right = Node(z)
        
#root->left->right        
def preorder(x):
    return f" {x.key}" + preorder(x.left) + preorder(x.right) if x else ""
#left-root-right
def inorder(x):
    return inorder(x.left) + f" {x.key}" + inorder(x.right) if x else ""
        
input()
#รับค่าทีละบรรทัด
node = {}
for s in sys.stdin:
    if s[0] == "p":
        #ถ้าเป็น p ก็ print ถ้าไม่เป็น p ดู ตน. 7 คือ ตัวเลข
        pass
        print(inorder(root))
        print(preorder(root))
    else:
        insert(int(s[7:]))

