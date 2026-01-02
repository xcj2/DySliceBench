import sys


class Node(object):
    __slots__ = ['value', 'parent', 'left', 'right']
    
    def __init__(self, value: int, parent: 'Node' = None):
        self.value = value
        self.parent = parent
        self.left: Node = None
        self.right: Node = None

    def walk(self, a, walk_type):
        if walk_type == 0:
            a.append(self.value)
        if self.left:
            self.left.walk(a, walk_type)
        if walk_type == 1:
            a.append(self.value)
        if self.right:
            self.right.walk(a, walk_type)
        if walk_type == 2:
            a.append(self.value)
        return a


class BinarySearchTree(object):
    __slots__ = ['root']
    
    def __init__(self):
        self.root: Node = None

    def insert(self, x: int):
        if self.root is None:
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


def solve():
    tree = BinarySearchTree()
    input()
    for l in (l.split() for l in sys.stdin):
        if l[0] == "insert":
            tree.insert(int(l[1]))
        else:
            print('', *tree.root.walk([], 1))
            print('', *tree.root.walk([], 0))


if __name__ == "__main__":
    solve()
