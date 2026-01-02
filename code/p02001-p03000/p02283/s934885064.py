import sys


class Node(object):
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return "Not implemented yet."

    def __repr__(self):
        return self.__str__()


def insert(key, node):
    if key < node.key:
        if node.left is None:
            left_node = Node(key, node)
            node.left = left_node
        else:
            insert(key, node.left)
    else:
        if node.right is None:
            right_node = Node(key, node)
            node.right = right_node
        else:
            insert(key, node.right)


def print_preorder(node):
    print(" %d" % node.key, end="")
    if node.left is not None:
        print_preorder(node.left)
    if node.right is not None:
        print_preorder(node.right)


def print_inorder(node):
    if node.left is not None:
        print_inorder(node.left)
    print(" %d" % node.key, end="")
    if node.right is not None:
        print_inorder(node.right)


def main():
    lines = sys.stdin.readlines()
    root = Node()

    for order in lines[1:]:
        if order.startswith("insert"):
            command, key = order.strip().split(" ")
            key = int(key)
            if root.key is None:
                root.key = key
            else:
                insert(key, root)
        elif order.startswith("print"):
            print_inorder(root)
            print("")
            print_preorder(root)
            print("")

if __name__ == "__main__":
    main()