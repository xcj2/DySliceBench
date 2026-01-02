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
        
    def find(self, data):
        parent = self.root
        if parent is None:
            print("no\n")
            return
        while parent:
            if parent.data == data:
                print("yes\n")
                return
            parent = parent.left if data < parent.data else parent.right
        print("no\n")
        return
    
    def delete(self, data):
        target = self.root
        if target is None:
            return
        while target:
            if target.data == data:
                if target.right and target.left:
                    next_target = target.right
                    if next_target.left is None:
                        if target == self.root:
                            self.root = next_target
                        target.data = next_target.data
                        target.right = next_target.right
                        return
                    while next_target.left:
                        parent = next_target
                        next_target = next_target.left
                    if target == self.root:
                        self.root = next_target
                    target.data = next_target.data
                    parent.left = next_target.right
                    return
                else:
                    child = target.right or target.left
                    if target == self.root:
                        self.root = child
                        if child is None:
                            return
                    if child:
                        target.data, target.left, target.right = child.data, child.left, child.right
                    else:
                        if data < parent.data:
                            parent.left = None
                        else:
                            parent.right = None
                    return
            parent = target
            target = target.left  if data < target.data else target.right


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
        if operation[0] == "i":
            binary_search_tree.insert(int(num[0]))
        elif operation[0] == "f":
            binary_search_tree.find(int(num[0]))
        elif operation[0] == "d":
            binary_search_tree.delete(int(num[0]))
        elif binary_search_tree.root is not None:
            print_inorder(binary_search_tree.root)
            print("\n")
            print_preorder(binary_search_tree.root)
            print("\n")
