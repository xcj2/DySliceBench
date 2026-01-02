class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, z):
        p = None
        x = self.root
        while x != None:
            p = x
            if z.key < x.key : x = x.left
            else             : x = x.right
        z.p = p
        if p == None      : self.root = z
        elif z.key < p.key: p.left  = z
        else              : p.right = z
    def get_inorder_list(self):
        def _get_inorder_list(root):
            l = root.left
            r = root.right
            if l: yield from _get_inorder_list(l)
            yield root.key
            if r: yield from _get_inorder_list(r)
        yield from _get_inorder_list(self.root)
    def get_preorder_list(self):
        def _get_preorder_list(root):
            l = root.left
            r = root.right
            yield root.key
            if l: yield from _get_preorder_list(l)
            if r: yield from _get_preorder_list(r)
        yield from _get_preorder_list(self.root)
    def find(self, k):
        def _find(k, x):
            if x == None : return False
            if k == x.key: return True
            if k <  x.key: return _find(k, x.left)
            return _find(k, x.right)
        return _find(k, self.root)

class Node:
    def __init__(self, k):
        self.key = k
        self.p = None
        self.left = None
        self.right = None

if __name__=='__main__':
    m = int(input())

    T = BinarySearchTree()
    for _ in range(m):        
        op = input().split()
        if   op[0] == 'insert': T.insert( Node(int(op[1])) )
        elif op[0] == 'find':
            print("yes" if T.find(int(op[1])) else "no")
        else:
            print("",*T.get_inorder_list())
            print("",*T.get_preorder_list())