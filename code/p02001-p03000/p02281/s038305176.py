import sys


class Node(object):
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return "parent = %s, left = %s, right = %s" % (self.parent, self.left, self.right)

    def __repr__(self):
        return self.__str__()


def preorder_traverse(node_list, current):
    print(" %d" % current, end="")
    node = node_list[current]
    if node.left != -1:
        preorder_traverse(node_list, node.left)
    if node.right != -1:
        preorder_traverse(node_list, node.right)


def inorder_traverse(node_list, current):
    node = node_list[current]
    if node.left != -1:
        inorder_traverse(node_list, node.left)
    print(" %d" % current, end="")
    if node.right != -1:
        inorder_traverse(node_list, node.right)


def postorder_traverse(node_list, current):
    node = node_list[current]
    if node.left != -1:
        postorder_traverse(node_list, node.left)
    if node.right != -1:
        postorder_traverse(node_list, node.right)
    print(" %d" % current, end="")


def main():
    lines = sys.stdin.readlines()
    num_of_nodes = int(lines[0])
    node_list = [Node() for _ in range(num_of_nodes)]

    # Set filiation
    for line in lines[1:]:
        node_id, left, right = [int(x) for x in line.strip().split(" ")]
        node_list[node_id].left = left
        node_list[node_id].right = right

        if left != -1:
            node_list[left].parent = node_id
        if right != -1:
            node_list[right].parent = node_id

    # Find root node id
    for node_id, node in enumerate(node_list):
        if node.parent == -1:
            root = node_id
            break

    print("Preorder")
    preorder_traverse(node_list, root)
    print("\nInorder")
    inorder_traverse(node_list, root)
    print("\nPostorder")
    postorder_traverse(node_list, root)
    print("")

if __name__ == "__main__":
    main()