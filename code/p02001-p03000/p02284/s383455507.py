class Tree:
    root = None

    def insert(self, node):
        y = None
        x = self.root
        while x:
            y = x
            x = x.left if node.key < x.key else x.right

        if not y:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def print(self):
        print(' ', end='')
        print(*self.root.print_in())
        print(' ', end='')
        print(*self.root.print_pre())

    def find(self, node):
        y = None
        x = self.root
        while x:
            y = x
            if node.key == x.key:
              break
            elif node.key < x.key:
              x = x.left
            else:
              x = x.right
            
        
        if not y:
            print("no")
        elif node.key == y.key:
            print("yes")
        else:
            print("no")


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def print_pre(self):
        yield self.key
        if self.left:
            for k in self.left.print_pre(): yield k
        if self.right:
            for k in self.right.print_pre(): yield k

    def print_in(self):
        if self.left:
            for k in self.left.print_in(): yield k
        yield self.key
        if self.right:
            for k in self.right.print_in(): yield k


tree = Tree()
m = int(input())

while m:
    l = input().split()
    if len(l) == 2 and l[0] == "insert":
       tree.insert(Node(int(l[1])))
    elif len(l) == 2 and l[0] == "find":
       tree.find(Node(int(l[1])))
    else:
       tree.print()
    m -= 1
