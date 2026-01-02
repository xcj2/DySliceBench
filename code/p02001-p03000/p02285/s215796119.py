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
        z = self.root
        while z:
            if k == z.key: return z
            if k <  z.key: z = z.left
            else         : z = z.right
        return None

    def delete(self, k):
        def ldelete(z):
            if z.left and z.right:
                c = z.right
                while c:
                    next_node = c
                    c = c.left if c.left else c.right
                z_key_n = next_node.key
                ldelete(next_node)
                z.key = z_key_n
            else:
                c = z.left if z.left else z.right
                if   z.p == None    : self.root = c
                elif z.key < z.p.key: z.p.left  = c
                else                : z.p.right = c
                if c: c.p = z.p
        z = self.find(k)
        if z: ldelete(z)
# end class BinarySearchTree:

class Node:
    def __init__(self, k):
        self.key = k
        self.p = None
        self.left = None
        self.right = None
#end class Node:
       

if __name__=='__main__':
    m = int(input())

    T = BinarySearchTree()
    for _ in range(m):        
        op = input().split()
        if   op[0] == 'insert': T.insert( Node(int(op[1])) )
        elif op[0] == 'delete': T.delete( int(op[1]) )
        elif op[0] == 'find'  : print("yes" if T.find(int(op[1])) else "no")
        else:
            print("",*T.get_inorder_list())
            print("",*T.get_preorder_list())