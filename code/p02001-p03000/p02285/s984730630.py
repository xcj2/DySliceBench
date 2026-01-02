import sys
 
NIL = -1
 
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = NIL
        self.left = NIL
        self.right = NIL
 
class Tree:
    def __init__(self):
        self.root = NIL
 
    def insert(self, z):
        y = NIL
        x = self.root
 
        while x != NIL:
            y = x
 
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
 
        z.parent = y
 
        if y == NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, value, node):
        if node == NIL:
            return False
        elif node.key == value:
            return True
        elif value < node.key:
            # print('go to left')
            return self.find(value, node=node.left)
        else:
            # print('go to right')
            return self.find(value, node=node.right)

    def delete(self, value, node):
        if node == NIL:
            return None
        elif value < node.key:
            self.delete(value, node.left)
        elif value > node.key:
            self.delete(value, node.right)
        else:
            check = (node.left != NIL) + (node.right != NIL)

            if check == 0:
                if node.parent.left != NIL and node.parent.left.key == value:
                    node.parent.left = NIL
                else:
                    node.parent.right = NIL

            elif check == 1:
                if node.left != NIL:
                    child = node.left
                else:
                    child = node.right

                if node.parent.left != NIL and node.parent.left.key == value:
                    node.parent.left = child
                    child.parent = node.parent
                else:
                    node.parent.right = child
                    child.parent = node.parent

            else:
                jisetu = node.right

                while jisetu.left != NIL:
                    jisetu = jisetu.left

                node.key = jisetu.key
                self.delete(jisetu.key, jisetu)

    def inorder_walk(self, node):
        if node == NIL:
            return None
 
        if node.left != NIL:
            self.inorder_walk(node=node.left)
 
        print(' ' + str(node.key), end='')
 
        if node.right != NIL:
            self.inorder_walk(node=node.right)
 
    def preorder_walk(self, node):
        if node == NIL:
            return None
 
        print(' ' + str(node.key), end='')
 
        if node.left != NIL:
            self.preorder_walk(node=node.left)
 
        if node.right != NIL:
            self.preorder_walk(node=node.right)
 
    def show(self):
        self.inorder_walk(self.root)
        print()
        self.preorder_walk(self.root)
        print()
 
 
n = int(sys.stdin.readline())
T = Tree()
 
for i in range(n):
    line = sys.stdin.readline().split()

    if len(line) == 1:
        T.show()
    elif line[0] == 'insert':
        key = int(line[1])
        T.insert(Node(key))
    elif line[0] == 'find':
        key = int(line[1])
        print('yes' if T.find(key, T.root) else 'no')
    else:
        key = int(line[1])
        T.delete(key, T.root)