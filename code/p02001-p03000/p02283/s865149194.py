import sys
input = sys.stdin.readline
print = sys.stdout.write

class Node:
    __slots__ = ["data", "left", "right"]
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    __slots__ = ["root"]
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        parent = self.root
        if parent is None:
            self.root = Node(data)
            return
        while parent:
            parent_old = parent
            parent = parent.left if data < parent.data else parent.right
        if data < parent_old.data:
            parent_old.left = Node(data)
        else:
            parent_old.right = Node(data)


def print_preorder(node):
    print(" {}".format(node.data))
    if node.left:
        print_preorder(node.left)
    if node.right:
        print_preorder(node.right)

def print_inorder(node):
    if node.left:
        print_inorder(node.left)
    print(" {}".format(node.data))
    if node.right:
        print_inorder(node.right)

if __name__ == "__main__":
    n = int(input())
    binary_search_tree = BinarySearchTree()
    for _ in range(n):
        operation, *num = input().split()
        if num:
            binary_search_tree.insert(int(num[0]))
        elif binary_search_tree.root is not None:
            print_inorder(binary_search_tree.root)
            print("\n")
            print_preorder(binary_search_tree.root)
            print("\n")
