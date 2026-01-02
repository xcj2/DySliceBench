class Node:
    def __init__(self,key = None,left = None,right = None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self,t,key):
        if t.key == None:
            t.key = key
            return
        y = None 
        x = t
        while x is not None:
            y = x
            if key<x.key:x = x.left
            else        :x = x.right
        if y is None  :t = Node(key)
        elif key<y.key:y.left = Node(key)
        else          :y.right = Node(key)

    def find(self,t,key):
        x = t
        while x is not None:
            if x.key==key:return True
            if key<x.key:x = x.left
            else        :x = x.right
        return False

    def inorder(self):
        if self.left!=None:self.left.inorder()
        print (' %d'%self.key,end = '')
        if self.right!=None:self.right.inorder()

    def preorder(self):
        print (' %d'%self.key,end = '')
        if self.left!=None:self.left.preorder()
        if self.right!=None:self.right.preorder()

    def walk(self):
        self.inorder()
        print ()
        self.preorder()
        print ()


def main():
    Tree = Node()
    q = int(input())
    for _ in range(q):
        com = list(input().split())
        if com[0] == 'insert':
            Tree.insert(Tree,int(com[1]))
        elif com[0] == 'find':
            print('yes' if Tree.find(Tree,int(com[1])) else 'no')
        else :
            Tree.walk()

if __name__ == '__main__':
    main()


