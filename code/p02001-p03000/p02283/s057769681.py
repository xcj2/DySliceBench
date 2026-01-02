import sys
input = sys.stdin.readline
btree = []
root = None


class Node():
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def showInorder(node):
    if node.left is not None:
        showInorder(node.left)
    print(" {0}".format(str(node.key)), end="")
    if node.right is not None:
        showInorder(node.right)


def showPreorder(node):
    print(" {0}".format(node.key), end="")
    if node.left is not None:
        showPreorder(node.left)
    if node.right is not None:
        showPreorder(node.right)


def insert(key):
    global root
    z = Node(key, None, None, None)
    y = None
    x = root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left  # 左の子へ移動
        else:
            x = x.right  # 右の子へ移動

    z.parent = y

    if y is None:
        root = z
    elif z.key < y.key:
        y.left = z  # zをyの左の子にする
    else:
        y.right = z  # zをyの右の子にする


def showtree(root):
    showInorder(root)
    print()
    showPreorder(root)
    print()


def main():
    m = int(input())
    global root
    for i in range(m):

        operation = input().split()

        # print(operation)

        if operation[0] == 'insert':
            # print("insert!")
            insert(int(operation[1]))
        else:
            # print("show tree!")
            # print("root.key:{0} root.left:{1} root.right:{2}".format(root.key, root.left, root.right))
            showtree(root)


if __name__ == '__main__':
    main()

