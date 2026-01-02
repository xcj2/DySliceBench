class BinaryTreeNode():
    # __slots__ = ['left', 'right', 'val']
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val

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
        node = BinaryTreeNode(val=val)

        if y == None:
            self.root = node
        elif node.val < y.val:
            y.left = node
        else:
            y.right = node

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
    if op == 'print':
        print_elements(bst.inorder())
        print_elements(bst.preorder())
    else:
        num = int(op[7:])
        bst.insert(num)

