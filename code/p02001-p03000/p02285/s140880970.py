class BinaryTreeNode():
    def __init__(self, val, parent=None, left=None, right=None):
        self.parent = parent
        self.left = None
        self.right = None
        self.val = val

    def get_child_num(self):
        num = 0
        if self.left != None: num += 1
        if self.right != None: num += 1
        return num

    def get_successor(self):
        x = self
        if x.right != None:
            return x.right.get_minimum()

        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    def get_minimum(self):
        x = self
        while x.left != None:
            x = x.left
        return x

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, val):
        y = None
        x = self.root
        while x != None:
            y = x
            if val < x.val:
                x = x.left
            else:
                x = x.right
        node = BinaryTreeNode(val=val, parent=y)

        if y == None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

    def find(self, val):
        x = self.root
        while x != None:
            if x.val == val:
                return x
            elif x.val < val:
                x = x.right
            else:
                x = x.left
        return None

    def delete(self, val):
        z = self.find(val)
        if z == None: return

        y = None
        if z.get_child_num() < 2:
            y = z
        else:
            y = z.get_successor()

        x = None
        if y.left != None:
            x = y.left
        else:
            x = y.right

        if x != None:
            x.parent = y.parent

        if y.parent == None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.val = y.val

    def preorder(self):
        self.preorder_list = []
        self.preorder_bfs(self.root)
        return self.preorder_list

    def preorder_bfs(self, u):
        if u == None: return
        self.preorder_list.append(u.val)
        self.preorder_bfs(u.left)
        self.preorder_bfs(u.right)

    def inorder(self):
        self.inorder_list = []
        self.inorder_dfs(self.root)
        return self.inorder_list

    def inorder_dfs(self, u):
        if u == None: return
        self.inorder_dfs(u.left)
        self.inorder_list.append(u.val)
        self.inorder_dfs(u.right)

def print_elements(arr):
    print(' ' + ' '.join([str(item) for item in arr]))

m = int(input())
bst = BinarySearchTree()
for i in range(m):
    op = input()
    if op.startswith('insert'):
        num = int(op[7:])
        bst.insert(num)
    elif op.startswith('delete'):
        num = int(op[7:])
        bst.delete(num)
    elif op.startswith('find'):
        num = int(op[5:])
        if bst.find(num):
            print('yes')
        else:
            print('no')
    else:
        print_elements(bst.inorder())
        print_elements(bst.preorder())

