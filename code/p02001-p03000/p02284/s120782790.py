class Node:
    def __init__(self, key=-1, parent=-1, left=-1, right=-1):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def insert(t, z):
    x, y = t, -1
    while x != -1:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y

    if y == -1:
        t = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

    return t


def find(x, k):
    while x != -1 and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right

    return x


def print_tree(t):
    def in_order(z):
        if z == -1:
            return

        in_order(z.left)
        print(" {}".format(z.key), end="")
        in_order(z.right)

    def pre_order(z):
        if z == -1:
            return

        print(" {}".format(z.key), end="")
        pre_order(z.left)
        pre_order(z.right)

    in_order(t)
    print()
    pre_order(t)
    print()


def main():
    n = int(input())
    bst = -1

    for i in range(n):
        order = input().split()
        if order[0][0] == "i":
            bst = insert(bst, Node(int(order[1])))
        elif order[0][0] == "f":
            if find(bst, int(order[1])) == -1:
                print("no")
            else:
                print("yes")
        else:
            print_tree(bst)


if __name__ == '__main__':
    main()

