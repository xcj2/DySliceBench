
class Node():
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1


def preorder(id):
    print(" {}".format(id), end="")

    if Nodes[id].left != -1:
        preorder(Nodes[id].left)
    if Nodes[id].right != -1:
        preorder(Nodes[id].right)


def inorder(id):
    if Nodes[id].left != -1:
        inorder(Nodes[id].left)

    print(" {}".format(id), end="")

    if Nodes[id].right != -1:
        inorder(Nodes[id].right)


def postorder(id):
    if Nodes[id].left != -1:
        postorder(Nodes[id].left)

    if Nodes[id].right != -1:
        postorder(Nodes[id].right)

    print(" {}".format(id), end="")


def main():
    n = int(input())
    global Nodes
    Nodes = [Node() for i in range(n)]

    for i in range(n):
        id, *children = map(int, input().split())
        left = children[0]
        right = children[1]
        Nodes[id].left = left
        Nodes[id].right = right
        for child in children:
            if child != -1:
                Nodes[child].parent = id

    rootid = ""
    for i, node in enumerate(Nodes):
        if node.parent == -1:
            rootid = i

    print("Preorder")
    preorder(rootid)
    print()

    print("Inorder")
    inorder(rootid)
    print()

    print("Postorder")
    postorder(rootid)
    print()


if __name__ == '__main__':
    main()

