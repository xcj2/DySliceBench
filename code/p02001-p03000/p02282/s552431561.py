class Node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


def reconstruct(x, y):
    top = x[0]
    root = Node(top)
    # print("root:", top)

    mid = y.index(top)
    left = y[:mid]
    right = y[mid+1:]
    if len(left) > 0:
        root.left = reconstruct(x[1:mid+1], left)
    if len(right) > 0:
        root.right = reconstruct(x[mid+1:], right)

    return root


def postorder(L, node):
    if node is None:
        return
    postorder(L, node.left)
    postorder(L, node.right)
    L.append(node.x)


if __name__ == "__main__":
    input()
    preorder = input().split()
    inorder = input().split()
    root = reconstruct(preorder, inorder)
    L = []
    postorder(L, root)
    print(' '.join(L))