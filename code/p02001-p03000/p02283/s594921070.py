class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,x):
        z = Node(x)
        y = None
        x = self.root
        while x:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

    def print(self):
        print('',' '.join(map(str,self.root.inwalk())))
        print('',' '.join(map(str,self.root.prewalk())))


class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def prewalk(self):
        ret = [self.data]
        if self.left:
            ret += self.left.prewalk()
        if self.right:
            ret += self.right.prewalk()
        return ret
    
    def inwalk(self):
        ret = []
        if self.left:
            ret += self.left.inwalk()
        ret += [self.data]
        if self.right:
            ret += self.right.inwalk()
        return ret

    
tree = Tree()
n = int(input())
for _ in range(n):
    input_line = input()
    if input_line[0] == 'i':
        tree.insert(int(input_line.split()[1]))
    else:
        tree.print()

