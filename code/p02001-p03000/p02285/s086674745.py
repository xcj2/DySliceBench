import sys
input = sys.stdin.readline

class Node:
    __slots__ = ['value', 'parent', 'left', 'right']
    def __init__(self, value: int, parent: 'Node' = None):
        self.value = value
        self.parent = parent
        self.left: Node = None
        self.right: Node = None
    def inParse(self):
        if self.value == None:
            return
        if self.left != None:
            self.left.inParse()
        print(' {}'.format(self.value), end='')
        if self.right != None:
            self.right.inParse()
    def preParse(self):
        if self.value == None:
            return
        print(' {}'.format(self.value), end='')
        if self.left != None:
            self.left.preParse()
        if self.right != None:
            self.right.preParse()

class BinarySearchTree:
    __slots__ = ['root']
    def __init__(self):
        self.root: Node = None
    def insert(self, x: int):
        if self.root == None:
            self.root = Node(x)
            return
        parent, current = None, self.root
        while current:
            parent = current
            if x < current.value:
                current = current.left
            else:
                current = current.right
        if x < parent.value:
            parent.left = Node(x, parent)
        else:
            parent.right = Node(x, parent)
    def find(self, x: int):
        y = self.root
        while y != None and y.value != x:
            if y.value > x:
                y = y.left
            else:
                y = y.right
        return y
    def getMinimum(self, x: Node):
        while x.left != None:
            x = x.left
        return x
    def getSuccer(self, x: Node):
        if x.right != None:
            return self.getMinimum(x.right)
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y
    def deleteNode(self, z: Node):
        if z.left == None or z.right == None:
            y = z
        else:
            y = self.getSuccer(z)
        if y.left != None:
            x = y.left
        else:
            x = y.right
        if x != None:
            x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y.parent.left == y:
            y.parent.left = x
        else:
            y.parent.right = x
        if y != z:
            z.value = y.value
        
def main():
    tree = BinarySearchTree()
    n = int(input())
    for _ in range(n):
        inp = input()
        if inp[0] == 'i':
            com, num = inp.split()
            tree.insert(int(num))
        elif inp[0] == 'f':
            com, num = inp.split()
            if tree.find(int(num)):
                print('yes')
            else:
                print('no')
        elif inp[0] == 'd':
            com, num = inp.split()
            y = tree.find(int(num))
            tree.deleteNode(y)
        else:
            tree.root.inParse()
            print()
            tree.root.preParse()
            print()

if __name__=='__main__': main()
