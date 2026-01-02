class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        z = Node(key)
        y = None  # x?????????????´????????????°
        # z???parent???????´?
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        # z??????????????´??????????´?
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key):
        x = self.root
        while x and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def show(self):
        print(" ", end="")
        print(*list(map(str, self.root.inwalk())))
        print(" ", end="")
        print(*list(map(str, self.root.prewalk())))


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

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


tree = Tree()
n = int(input())
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == 'insert':
        tree.insert(int(cmd[1]))
    elif cmd[0] == 'find':
        if tree.find(int(cmd[1])):
            print("yes")
        else:
            print("no")
    elif cmd[0] == 'print':
        tree.show()