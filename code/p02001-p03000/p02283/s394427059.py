from typing import Optional


class Node:
    def __init__(self, arg_parent: Optional["Node"], arg_key: int,
                 arg_left: Optional["Node"], arg_right: Optional["Node"]):
        self.parent = arg_parent
        self.key = arg_key
        self.left = arg_left
        self.right = arg_right


def print_preorder(node: Node) -> None:
    print(f" {node.key}", end="")
    if node.left is not None:
        print_preorder(node.left)
    if node.right is not None:
        print_preorder(node.right)


def print_inorder(node: Node) -> None:
    if node.left is not None:
        print_inorder(node.left)
    print(f" {node.key}", end="")
    if node.right is not None:
        print_inorder(node.right)


def insert(root: Optional[Node], node: Node) -> Node:
    y: Optional[Node] = None
    x = root

    while x is not None:
        y = x
        if node.key < x.key:
            x = x.left
        else:
            x = x.right
    node.parent = y

    if y is None:
        root = node
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node

    assert root is not None
    return root


if __name__ == "__main__":
    root: Optional[Node] = None
    node_num = int(input())
    for _ in range(node_num):
        command, *value = input().split()
        if "insert" == command:
            root = insert(root, Node(None, int(value[0]), None, None))
        elif "print" == command:
            assert root is not None
            print_inorder(root)
            print()
            print_preorder(root)
            print()
        else:
            pass

