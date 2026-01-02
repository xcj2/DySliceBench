import sys


class Node:
    left = None
    right = None
    key = None

    def __init__(self, key):
        self.key = key
        return


class Tree:

    def __init__(self):
        self.root = None


def insert(T, z):
    '''
    T : Tree
    z : 要素
    '''

    p = None  # x の親（を入れる変数）
    x = T.root

    while x:  # 子がいなかったら
        p = x  # 親を設定
        if z.key < x.key:
            x = x.left  # 左の子へ移動
        else:
            x = x.right  # 右の子へ移動

    if p is None:  # T が空の場合
        T.root = z
    elif z.key < p.key:
        p.left = z  # z を y の左の子にする
    else:
        p.right = z  # z を y の右の子にする


def inorder(v):

    if v.left is not None:
        inorder(v.left)

    print("", v.key, end="")

    if v.right is not None:
        inorder(v.right)

    return


def preorder(r):

    print("", r.key, end="")

    if r.left is not None:
        preorder(r.left)
    if r.right is not None:
        preorder(r.right)

    return


def display(v):

    inorder(v)
    print("")
    preorder(v)
    print("")
    return


def main():

    T = Tree()

    # print(T)

    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        op = sys.stdin.readline().rstrip().split()

        if len(op) == 2:
            v = Node(int(op[1]))
            insert(T, v)

        if len(op) == 1:
            display(T.root)


main()

