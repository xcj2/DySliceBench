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
        Ny = None  # ???????£?
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

    def find(self, key):
        Nx = self.root
        while Nx and Nx.key != key:
            if key < Nx.key:
                Nx = Nx.left
            else:
                Nx = Nx.right
        return Nx

    def delete(self, key):
        Nz = self.find(key)
        # Ny: the node to be deleted
        if Nz.left and Nz.right:
            Ny = self.successor(Nz)
        else:
            Ny = Nz
        # Nx: y's child
        if Ny.left:
            Nx = Ny.left
        else:
            Nx = Ny.right

        if Nx:
            Nx.parent = Ny.parent

        if Ny.parent == None:
            self.root = Nx
        elif Ny == Ny.parent.left:
            Ny.parent.left = Nx
        else:
            Ny.parent.right = Nx

        if Ny != Nz:
            Nz.key = Ny.key

    def successor(self, Nx):
        if Nx.right:
            return self.minimum(Nx.right)

        Ny = Nx.parent
        while Ny != None and Nx == Ny.right:
            Nx = Ny
            Ny = Ny.parent
        return Ny

    def minimum(self, Nx):
        while Nx.left:
            Nx = Nx.left
        return Nx

    def print(self):
        print('', ' '.join(map(str, self.root.inwalk())))
        print('', ' '.join(map(str, self.root.prewalk())))

tree = Tree()

n = sys.stdin.readline()
for line in sys.stdin:
    if line[0] == 'i':
        tree.insert(int(line.split()[1]))
    elif line[0] == 'f':
        if tree.find(int(line.split()[1])):
            print('yes')
        else:
            print('no')
    elif line[0] == 'd':
        tree.delete(int(line.split()[1]))
    else:
        tree.print()