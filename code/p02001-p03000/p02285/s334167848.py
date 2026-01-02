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
            node.parent = y
        else:
            y.right = node
            node.parent = y

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
            return y
        else:
            print("no")

    def delete1(self, node):
        y = node.parent
        if y.key < node.key:
          y.right = None
        elif y.key > node.key:
          y.left = None
        node.parent = None

    def delete2(self, node):
        y = node.parent
        if y.key < node.key:
          y.right = node.right
        else:
          y.left = node.right
        node.right.parent = y

    def delete3(self, node):
        y = node.parent
        if y.key < node.key:
          y.right = node.left
        else:
          y.left = node.left
        node.left.parent = y
    
    def delete4(self, node):
        y = node.right
        x = y
        while x.left:
          x = x.left

        node.key = x.key
        if y == x:
          node.right = None
          
        if not x.left and not x.right:
          self.delete1(x)
        elif not x.left and x.right:
          self.delete2(x)
        else:
          self.delete3(x)

    def delete(self, node):
        y = self.find(node)
        if y:
          if not y.left and not y.right:
             self.delete1(y)

          elif not y.left and y.right:
             self.delete2(y)
        
          elif y.left and not y.right:
             self.delete3(y)

          else:
             self.delete4(y)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None

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
       y = tree.find(Node(int(l[1])))
       if y:
          print("yes")
    elif len(l) == 2 and l[0] == "delete":
       tree.delete(Node(int(l[1])))
    else:
       tree.print()
    m -= 1
