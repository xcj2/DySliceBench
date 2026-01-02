# coding: utf-8

class Node:
    def __init__(self, key, priority, left=None, right=None):
        self.key = key
        self.priority = priority
        self.left = left
        self.right = right
        self.parent = None
        self.ans = []

class Treap:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node, key, priority):
        if node == None:
            return Node(key, priority)
        if key == node.key:
            return node
        
        if key < node.key:
            node.left = self.insert(node.left, key, priority)
            if node.priority < node.left.priority:
                node = self.rightRotate(node)
        else:
            node.right = self.insert(node.right, key, priority)
            if node.priority < node.right.priority:
                node = self.leftRotate(node)
        return node
            
        
    def rightRotate(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        return tmp
        
    def leftRotate(self, node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        return tmp
    
    def delete(self, node, key):
        if node == None:
            return None
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            return self._delete(node, key)
        return node
    
    def _delete(self, node, key):
        if node.left == None and node.right == None:
            return None
        elif node.left == None:
            node = self.leftRotate(node)
        elif node.right == None:
            node = self.rightRotate(node)
        else:
            if node.left.priority > node.right.priority:
                node = self.rightRotate(node)
            else:
                node = self.leftRotate(node)
        return self.delete(node, key)
        
    def find(self, node, key):
        if key == node.key:
            return node
        if key < node.key:
            if node.left != None:
                return self.find(node.left, key)
            else:
                return None
        if key > node.key:
            if node.right != None:
                return self.find(node.right, key)
            else:
                return None
    
    def resetAns(self):
        self.ans = []
    
    def getPreorder(self, node):
        self.ans.append(node)
        if node.left != None:
            self.getPreorder(node.left)
        if node.right != None:
            self.getPreorder(node.right)
    
    def getInorder(self, node):
        if node.left != None:
            self.getInorder(node.left)
        self.ans.append(node)
        if node.right != None:
            self.getInorder(node.right)
            
    def printAns(self):
        for nd in self.ans:
            print(" " + str(nd.key),end="")
        print()

m = int(input().rstrip())
tr = Treap()
for i in range(m):
    line = input().rstrip().split()
    if line[0] == "insert":
        tr.root = tr.insert(tr.root, int(line[1]), int(line[2]))
    elif line[0] == "find":
        if tr.find(tr.root, int(line[1])) != None:
            print("yes")
        else:
            print("no")
    elif line[0] == "delete":
        tr.root = tr.delete(tr.root, int(line[1]))
    else:
        tr.resetAns()
        tr.getInorder(tr.root)
        tr.printAns()
        tr.resetAns()
        tr.getPreorder(tr.root)
        tr.printAns()
