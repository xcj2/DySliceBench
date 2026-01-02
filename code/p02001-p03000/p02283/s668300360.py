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

def main():
    tree = BinarySearchTree()
    n = int(input())
    for _ in range(n):
        inp = input()
        if inp[0] == 'i':
            com, num = inp.split()
            tree.insert(int(num))
        else:
            tree.root.inParse()
            print()
            tree.root.preParse()
            print()

if __name__=='__main__': main()
