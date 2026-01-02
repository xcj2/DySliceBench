class Node:
    def __init__(self, k, p):
        self.k, self.p = k, p
        self.left, self.right = None, None

class Treap:
    def __init__(self):
        self.root = None
    
    def insert(self, k, p):
        self.root = self.__insert(self.root, k, p)

    def rightRotate(self, t):
        s = t.left
        t.left = s.right
        s.right = t
        return s
    
    def leftRotate(self, t):
        s = t.right
        t.right = s.left
        s.left = t
        return s

    def __insert(self, t, k , p):
        if t == None:
            return Node(k, p)
        if k == t.k:
            return t
        
        if k < t.k:
            t.left = self.__insert(t.left, k, p)
            if t.p < t.left.p:
                t = self.rightRotate(t)
        else:
            t.right = self.__insert(t.right, k, p)
            if t.p < t.right.p:
                t = self.leftRotate(t)
        return t
    
    def delete(self, k):
        self.root = self._delete(k)
        
    def _delete(self, k, t = -1):
        if t == -1:
            t = self.root
        
        if t == None:
            return None
        if k < t.k:
            t.left = self._delete(k, t.left)
        elif k > t.k:
            t.right = self._delete(k, t.right)
        else:
            return self.__delete(t, k)
        return t
    
    def __delete(self, t, k):
        if t.left == None and t.right == None:
            return None
        elif t.left == None:
            t = self.leftRotate(t)
        elif t.right == None:
            t = self.rightRotate(t)
        else:
            if t.left.p > t.right.p:
                t = self.rightRotate(t)
            else:
                t = self.leftRotate(t)
        return self._delete(k, t)

    def find(self, k, t = -1):
        if t == -1:
            t = self.root
        if t == None:
            return None
        if k < t.k:
            return self.find(k, t.left)
        elif k > t.k:
            return self.find(k, t.right)
        else:
            return t
    
    def preOrder(self, r = -1):
        if r == -1: r = self.root
        if r == None:   return
        print("", r.k, end = '')
        self.preOrder(r.left)
        self.preOrder(r.right)
    
    def inOrder(self, r = -1):
        if r == -1: r = self.root
        if r == None:   return
        self.inOrder(r.left)
        print("", r.k, end = '')
        self.inOrder(r.right)
    
    def print(self):
        self.inOrder()
        print()
        self.preOrder()
        print()

tree = Treap()
for _ in range(int(input())):
    In = input().split()
    if In[0][0] == 'i':
        tree.insert(int(In[1]), int(In[2]))
    elif In[0][0] == 'p':
        tree.print()
    elif In[0][0] == 'f':
        print(['no', 'yes'][tree.find(int(In[1])) != None])
    elif In[0][0] == 'd':
        tree.delete(int(In[1]))

