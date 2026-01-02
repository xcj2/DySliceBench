class Node:
    def __init__(self):
        self.key, self.left, self.right, self.parent = 0, None, None, None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        x, y = self.root, None
        z = Node()
        z.key = key
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    
    def find(self, key):
        r = self.root
        while r != None:
            if key == r.key:
                break
            elif key < r.key:
                r = r.left
            else:
                r = r.right
        return r
    
    def delete(self, key, r = -1):
        if r == -1:
            r = self.root
        if r == None:
            return None
        if r.key == key:
            if r.left == r.right == None:
                p = r.parent
                if p == None:
                    self.root = None
                    return None
                return None
            elif r.left != None and r.right != None:
                s = self.successor(r)
                r.key = s.key
                r.right = self.delete(s.key, r.right)
                return r
            elif r.left != None:
                p = r.parent
                if p == None:
                    self.root =r.left
                    r.left.p = None
                    return r.left
                if p.left == r:
                    p.left = r.left
                    r.left.parent = p
                else:
                    p.right = r.left
                    r.left.parent = p
                return r.left
            elif r.right != None:
                p = r.parent
                if p == None:
                    self.root = r.right
                    r.right.p = None
                    return r.right
                if p.left == r:
                    p.left = r.right
                    r.right.parent = p
                else:
                    p.right = r.right
                    r.right.parent = p
                return r.right
        elif r.key < key:
            r.right = self.delete(key, r.right)
        else:
            r.left = self.delete(key, r.left)
        return r

    def successor(self, r):
        r = r.right
        if r == None:
            return None
        while r.left != None:
            r = r.left
        return r
    
    def preOrder(self, r = -1):
        if r == -1: r = self.root
        if r == None:   return
        print("", r.key, end = '')
        self.preOrder(r.left)
        self.preOrder(r.right)
    
    def inOrder(self, r = -1):
        if r == -1: r = self.root
        if r == None:   return
        self.inOrder(r.left)
        print("", r.key, end = '')
        self.inOrder(r.right)

tree = BST()
for _ in range(int(input())):
    s = input()
    if s[0] == 'i':
        tree.insert(int(s[7:]))
    elif s[0] == 'p':
        tree.inOrder()
        print("")
        tree.preOrder()
        print("")
    elif s[0] == 'f':
        print(['no', 'yes'][tree.find(int(s[5:])) != None])
    else:
        tree.delete(int(s[7:]))
