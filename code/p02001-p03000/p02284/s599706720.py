import sys
class Tree():
    def __init__(self):
        self.root = None
    def insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        while x:
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
        x = self.root
        while x and x.key != key:
            if x.key < key:
                x = x.right
            else:
                x = x.left
        print('yes' if x else 'no')
    def print(self):
        print('',' '.join(map(str, self.root.inwalk())))
        print('',' '.join(map(str, self.root.prewalk())))
    
class Node():
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
    def prewalk(self):
        ret = [self.key]
        if self.left:
            ret += self.left.prewalk()
        if self.right:
            ret += self.right.prewalk()
        return ret
    def inwalk(self):
        ret = []
        if self.left:
            ret += self.left.inwalk()
        ret += [self.key]
        if self.right:
            ret += self.right.inwalk()
        return ret
tree = Tree()
n = sys.stdin.readline()
for line in sys.stdin:
    if line[0] == 'i':
        tree.insert(int(line.split()[1]))
    elif line[0] == 'f':
        tree.find(int(line.split()[1]))
    else:
        tree.print()