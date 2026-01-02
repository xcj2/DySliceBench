import sys
input = sys.stdin.readline
print = sys.stdout.write

class Node:
    __slots__ = ["key", "priority", "left", "right"]
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        
class Treap:
    def insert(self, node, key, priority):
        if node is None:
            return Node(key, priority)
        if key == node.key:
            return node
        if key < node.key:
            node.left = self.insert(node.left, key, priority)
            if node.priority < node.left.priority:
                node = right_rotate(node)
        else:
            node.right = self.insert(node.right, key, priority)
            if node.priority < node.right.priority:
                node = left_rotate(node)
        return node

    def delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            return self._delete(node, key)
        return node
    
    def _delete(self, node, key):
        if node.left is None and node.right is None:
            return None
        if node.left is None:
            node = left_rotate(node)
        elif node.right is None:
            node = right_rotate(node)
        else:
            if node.left.priority > node.right.priority:
                node = right_rotate(node)
            else:
                node = left_rotate(node)
        return self.delete(node, key)
    
    def find(self, node, key):
        if node is None:
            print("no\n")
            return
        while node:
            if node.key == key:
                print("yes\n")
                return
            node = node.left if key < node.key else node.right
        print("no\n")
        return
            

def right_rotate(node):
    child = node.left
    node.left, child.right = child.right, node
    return child

def left_rotate(node):
    child = node.right
    node.right, child.left = child.left, node
    return child

def print_preorder(node):
    print(" {}".format(node.key))
    if node.left:
        print_preorder(node.left)
    if node.right:
        print_preorder(node.right)

def print_inorder(node):
    if node.left:
        print_inorder(node.left)
    print(" {}".format(node.key))
    if node.right:
        print_inorder(node.right)

if __name__ == "__main__":
    n = int(input())
    treap = Treap()
    root = None
    for _ in range(n):
        operation, *num = input().split()
        if operation[0] == "i":
            root = treap.insert(root, int(num[0]), int(num[1]))
        elif operation[0] == "f":
            treap.find(root, int(num[0]))
        elif operation[0] == "d":
            root = treap.delete(root, int(num[0]))
        elif root is not None:
            print_inorder(root)
            print("\n")
            print_preorder(root)
            print("\n")
