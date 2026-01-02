import sys

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def prewalk(self):
        nodeList = [self.key]
        if self.left:
            nodeList += self.left.prewalk()
        if self.right:
            nodeList += self.right.prewalk()
        return nodeList

    def inwalk(self):
        nodeList = []
        if self.left:
            nodeList += self.left.inwalk()
        nodeList += [self.key]
        if self.right:
            nodeList += self.right.inwalk()
        return nodeList

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        Nz = Node(key)
        Ny = None #???????£?
        Nx = self.root
        while Nx:
            Ny = Nx
            if Nz.key < Ny.key:
                Nx = Nx.left
            else:
                Nx = Nx.right
        Nz.parent = Ny
        if Ny == None:
            self.root = Nz
        elif Nz.key < Ny.key:
            Ny.left = Nz
        else:
            Ny.right = Nz

    def print(self):
        print('', ' '.join(map(str, self.root.inwalk())))
        print('', ' '.join(map(str, self.root.prewalk())))

tree = Tree()

n = sys.stdin.readline()
for line in sys.stdin:
    if line[0] == 'i':
        tree.insert(int(line.split()[1]))
    else:
        tree.print()