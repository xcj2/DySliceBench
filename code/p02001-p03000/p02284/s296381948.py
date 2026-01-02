class node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.key = None
        
class btree:
    def __init__(self):
        self.root = None
        
    def insert(self, v):
        y = None
        x = self.root
        z = node()
        z.key = v
        
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    
    def find(self, v):
        x = self.root
        z = node()
        z.key = v
        
        find_flg = 0
        while x is not None:
            if x.key == z.key:
                find_flg = 1
                break

            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        
        if find_flg:
            print('yes')
        else:
            print('no')
    

    def print_tree(self):
        def inorder(nd):
            if nd.left is not None:
                inorder(nd.left)
            print(' %i'%nd.key, end='')
            if nd.right is not None:
                inorder(nd.right)
        
        def preorder(nd):
            print(' %i'%nd.key, end='')
            if nd.left is not None:
                preorder(nd.left)
            if nd.right is not None:
                preorder(nd.right)
                
        inorder(self.root)
        print()
        preorder(self.root)
        print()
        
n = int(input())

bt = btree()

for i in range(n):
    inp = input()
    if inp.split()[0]=='insert':
        bt.insert(int(inp.split()[1]))
    elif inp.split()[0]=='find':
        bt.find(int(inp.split()[1]))
    else:
        bt.print_tree()
        
